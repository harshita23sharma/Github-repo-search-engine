import pymongo
from pymongo import MongoClient
import pandas as pd
import nltk
import numpy as np
# from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re
import pprint
import os
import fnmatch
import imp
import config_index

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
CONFIG = '/config.py'

PATH = str(d) + CONFIG
foo = imp.load_source('config.py', PATH)
print(foo.INDEX_NAME)
h = foo.INDEX_NAME
db = pymongo.MongoClient().h
FOLDER = '/haproxy'
# print(os.pardir)
root = str(d) + FOLDER
count = 0
for path, subdirs, files in os.walk(root):
    print("path...  ",path)
    print("subdirs.....  ",subdirs)
    print("files....  ",files)
    for name in files:
        if fnmatch.fnmatch(name, '*.c'):            
            path = os.path.join(path, name)
            try:
                print(1)
                f = open(path)
                print(2) # open a file
                text = f.read() # read the entire contents, should be UTF-8 text
    #             build a document to be inserted
                print(3)
                text_file_doc = {"file_name": name, "contents" : text ,"_id":count}
    #             insert the contents into the "file" collection
                print(5)
                db.test.insert(text_file_doc)
                print(6)
                count +=1
            # db.fs.chunks.createIndex( { files_id: 1, n: 1 }, { unique: true } );
                print(name)
                print("------------------------")
            except Exception as e:
                # print(e)
                # print(" ")
    #             count +=1
                continue
