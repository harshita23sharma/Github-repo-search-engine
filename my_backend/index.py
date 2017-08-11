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
import fnmatch
import config_index

client = MongoClient()
db = client[config_index.INDEX_NAME]
FOLDER = config_index.INPUT_FOLDER
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
root = str(d) + FOLDER
count = 0
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch.fnmatch(name, '*.c'):            
            path2 = os.path.join(path, name)
            try:
                f = open(path2)  # open a file
                text = f.read() # read the entire contents, should be UTF-8 text
    #             build a document to be inserted
                text_file_doc = {"file_name": name, "contents" : text ,"_id":count}
                db.test.insert(text_file_doc)
                count +=1
                print("------------------------",count)
            except Exception as e:
                continue