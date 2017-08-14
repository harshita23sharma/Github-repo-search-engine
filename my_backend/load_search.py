import pymongo
from pymongo import MongoClient
import pandas as pd
import nltk
import numpy as np
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re
import pprint
import os
import config_index
MATRIX_PATH = '/my_backend/' + config_index.MATRIX_NAME

def find_file(q_param):
	file_list = []
	new_data = []
	client = MongoClient()
	db = client[config_index.INDEX_NAME]
	ans = []
	for count in range(config_index.FILES_COUNT):
		new_dict = {}
		cur = db.test.find({"_id":count})
		pp = pprint.PrettyPrinter()
		try:
			for i in cur:	
				raw_review = i['contents']
				review_text = raw_review
				letters_only = re.sub("[^a-zA-Z0-9_*]", " ", review_text)
				words = letters_only.split()
				ans.extend(words)
		except Exception as e:
			print("inside except",e)
			ans.extend(e)
	corpus = list(set(ans))
	corpus.sort()
	
	FILE_MATRIX_PATH = config_index.WORKING_DIR + MATRIX_PATH
	file_name = FILE_MATRIX_PATH 
	df = pd.read_pickle(file_name)
	df.fillna(0,inplace =True)
	col_names = df.columns
	df1 = df
	df3 = pd.DataFrame(columns=["q"],index=corpus)
	df3.fillna('0',inplace =True)

	letters_only = re.sub("[^a-zA-Z0-9_*]", " ", q_param)
	q_words = letters_only.split()
	for q_param in q_words:
		try:
			df3.loc[[str(q_param)]]=1
		except Exception as e:
			print(e)
	file_list_filter = []
	for i in col_names:
		count = df.astype(bool)
		for q_param in q_words:
			if df.loc[str(q_param)][i] == 0:
				break
			else:
				file_list_filter.append(i)
	try:
		df4 = df3.transpose()
		df_final= df4.astype(float).dot(df1.astype(float))
		a = df_final.to_dict()
		from collections import OrderedDict

		ordered = OrderedDict(sorted(a.items(), key=lambda i: i[1]['q'], reverse=True))

		file_list = []
		for odict in ordered:
		    if ordered[odict]['q'] != 0.0:
		    	file_list.append(odict)
		        # print("odict,ordered[odict]['q']",odict,ordered[odict]['q'])
		# a = df_final.idxmax(axis=1, skipna=True)
		for i in file_list_filter:
			if i not in file_list:
				print(i," not in file-> ",file_list)
				file_list_filter.remove(i)
				print("so now file list is",file_list_filter)
		contents = " "
		if len(file_list_filter) != 0:
			ans = file_list_filter[0]

			print("ANSWER IS...",ans)
			print("  ")
			cur2 = db.test.find({"file_name":ans})			
			for k in cur2:
				contents = k["contents"]

		pattern='[;](.*?)(\s)*(' +str(q_param) + '(\s)*)(.*?)[;]'
		# pattern = ';(.)*(' + str(q_param) + ')(.)*?;' # non greedy gives everything between two ; semicolons
		# pattern = ';([;{#]*[\s\S])*?(.)*?(' + str(q_param) + ')(.)*(\n)*?[;]*'
		grams = re.findall(pattern, contents)
		new_data = "  ".join([i for sub in grams for i in sub])
		
		if len(new_data)==0 :
			return(list(set(file_list_filter)),contents)
		else:
			return(list(set(file_list_filter)),new_data)


	except Exception as e:
		ee = []
		ee.append(e)
		return ee,ee

    