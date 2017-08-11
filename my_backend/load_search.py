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
	
	FILE_MATRIX_PATH = config_index.WORKING_DIR + MATRIX_PATH

	print("FILE_MATRIX_PATH  ",FILE_MATRIX_PATH)
	file_name = FILE_MATRIX_PATH 
	df = pd.read_pickle(file_name)
	df.fillna(0,inplace =True)

	df1 = df
	print(df.head())
	df3 = pd.DataFrame(columns=["q"],index=corpus)
	df3.fillna('0',inplace =True)
	try:
		df3.loc[[str(q_param)]]=1
		df4 = df3.transpose()
		df_final= df4.astype(float).dot(df1.astype(float))
		a = df_final.idxmax(axis=1, skipna=True)
		print("ANSWER IS...",a['q'])
		print("  ")
		cur2 = db.test.find({"file_name":a['q']})
		for k in cur2:
			contents = k["contents"]
		pattern='[;](.*?)(\s)*(' +str(q_param) + '(\s)*)(.*?)[;]'
		# pattern = ';(.)*(' + str(q_param) + ')(.)*?;' # non greedy gives everything between two ; semicolons
		# pattern = ';([;{#]*[\s\S])*?(.)*?(' + str(q_param) + ')(.)*(\n)*?[;]*'
		grams = re.findall(pattern, contents)
		new_data = "  ".join([i for sub in grams for i in sub])

		if len(new_data)==0 :
			return(a['q'],contents)
		else:
			return(a['q'],new_data)

	except Exception as e:
		return e,e

    