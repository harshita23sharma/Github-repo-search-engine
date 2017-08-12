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
				letters_only = re.sub("[^a-zA-Z0-9_]", " ", review_text)
				words = letters_only.split()
				ans.extend(words)
		except Exception as e:
			print("inside except",e)
			ans.extend(e)
	corpus = list(set(ans))
	corpus.sort()
	for i in corpus:
		if i == "REGPRM3" :
			print("REGPRM3 is present at ",i)
	print("no result....")
	
	FILE_MATRIX_PATH = config_index.WORKING_DIR + MATRIX_PATH

	print("FILE_MATRIX_PATH  ",FILE_MATRIX_PATH)
	file_name = FILE_MATRIX_PATH 
	df = pd.read_pickle(file_name)
	df.fillna(0,inplace =True)

	df1 = df
	print(df.head())
	df3 = pd.DataFrame(columns=["q"],index=corpus)
	df3.fillna('0',inplace =True)

	letters_only = re.sub("[^a-zA-Z0-9_]", " ", q_param)
	q_words = letters_only.split()
	for q_param in q_words:
		try:
			df3.loc[[str(q_param)]]=1
			print("df3.loc[[str(q_param)]]   ....   ....   ....  ",df3.loc[[str(q_param)]])
		except Exception as e:
			print(e)
	print(df3.head())
	try:
		# df3.loc[[str(q_param)]]=1
		df4 = df3.transpose()
		df_final= df4.astype(float).dot(df1.astype(float))
		a = df_final.to_dict()
		print("a is...........................  ",a)
		from collections import OrderedDict

		ordered = OrderedDict(sorted(a.items(), key=lambda i: i[1]['q'], reverse=True))
		print("ordered dict is...............   ",ordered)


		# if any(word in 'some one long two phrase three' for word in list_):

		
		file_list = []
		for odict in ordered:
		    if ordered[odict]['q'] != 0.0:
		    	file_list.append(odict)
		        print("odict,ordered[odict]['q']",odict,ordered[odict]['q'])
		# a = df_final.idxmax(axis=1, skipna=True)
		
		contents = " "
		if len(file_list) != 0:
			ans = file_list[0]

			print("ANSWER IS...",ans)
			print("  ")
			cur2 = db.test.find({"file_name":ans})
			print("cur2 is.. " ,cur2)
			
			for k in cur2:
				contents = k["contents"]

		# pattern='[;](.*?)(\s)*(' +str(q_param) + '(\s)*)(.*?)[;]'
		# # pattern = ';(.)*(' + str(q_param) + ')(.)*?;' # non greedy gives everything between two ; semicolons
		# # pattern = ';([;{#]*[\s\S])*?(.)*?(' + str(q_param) + ')(.)*(\n)*?[;]*'
		# grams = re.findall(pattern, contents)
		# new_data = "  ".join([i for sub in grams for i in sub])
		
		print(type(contents))
		if len(new_data)==0 :
			return(file_list,contents)
		else:
			return(file_list,new_data)


	except Exception as e:
		ee = []
		ee.append(e)
		return ee,ee

    