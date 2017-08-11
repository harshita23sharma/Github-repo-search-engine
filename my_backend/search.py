import pymongo
from pymongo import MongoClient
import pandas as pd
import nltk
import numpy as np
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re
import pprint
import config_index

# db = pymongo.MongoClient().config.INDEX_NAME
# db = pymongo.MongoClient().test_bulk_ex
client = MongoClient()
db = client[config_index.INDEX_NAME]

col_names = db.test.distinct('file_name')
print(col_names)

fin_dict = {}
ans = []
for count in range(105):
    ans2 = []
    new_dict = {}
    cur = db.test.find({"_id":count})
    pp = pprint.PrettyPrinter()
    for i in cur:
        raw_review = i['contents']
        review_text = raw_review
        letters_only = re.sub("[^a-zA-Z0-9_]", " ", review_text)
        words = letters_only.split()
        ans2.extend(words)
        ans.extend(words)
        new_dict[i["file_name"]]=ans2
        fin_dict.update(new_dict)
pprint.pprint(fin_dict)

corpus = list(set(ans))
corpus.sort()
print(corpus)
df = pd.DataFrame(columns=col_names,index=corpus)

def append_value_to_key(my_d,k,v):
    if k in my_d:
        my_d[k].append(v)
    else:
        my_d[k]=[v]
    return my_d
            
def append_dict_to_dict(in_dict , ex_dict):
    for k in ex_dict:
        if k in in_dict:
            in_dict[k].append(ex_dict[k])
        else:
            in_dict[k] = [ex_dict[k]]

cur = db.test.find()
ans = []
term_doc_dict = {}

for count in range(35):
    appended_dict = {}
    ans = []
    cur = db.test.find({"_id":count})
    pp = pprint.PrettyPrinter()
    for i in cur:
        prev_dict = {}
        raw_review = i['contents']
        review_text = raw_review
        letters_only = re.sub("[^a-zA-Z0-9_]", " ", review_text)
        words = letters_only.split()
        for k in words:
            appended_dict = append_value_to_key(prev_dict,k,i["file_name"])
        append_dict_to_dict(term_doc_dict , appended_dict)
        
print(term_doc_dict)

for i in term_doc_dict:
    for sub_list in term_doc_dict[i]:
        l = len(sub_list)
        name= sub_list[0]
        df.loc[i,name]=l

print("df")
print(df)
# file_name = "my_matrix.pkl"
# df.to_pickle(file_name)

df2 = pd.DataFrame(columns=col_names,index=corpus)

for i in term_doc_dict:
    for sub_list in term_doc_dict[i]:
        l = len(sub_list)
        name= sub_list[0]
        df2.loc[i,name]=l

print("df")
print(df2)
file_name = config_index.MATRIX_NAME
df2.to_pickle(config_index.MATRIX_NAME)
df = pd.read_pickle(file_name)
df.fillna(0,inplace =True)

df1 = df

# query_term = "old_sig"
df3 = pd.DataFrame(columns=["q"],index=corpus)
df3.fillna('0',inplace =True)
df3.loc[["never"]]=1
df4 = df3.transpose()
df_final= df4.astype(float).dot(df1.astype(float))
a = df_final.idxmax(axis=1, skipna=True)
print("ANSWER IS...",a['q'])
