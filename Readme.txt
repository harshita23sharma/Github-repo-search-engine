#Search Engine for Single Exact keywords (version1)

Setting up the Python environment
---
First, install the following packages.

```bash
sudo apt-get install build-essential python-dev python-pip
```

Python 2.7.6
MongoDB server version: 3.4.6

''' bash
cd search  # cd projectfolder
virtualenv testenv
source testenv/bin/activate

sudo pip2 install -r requirements.txt
sudo apt-get install xvfb
'''

''' SET PATHS :

config.py
mybackend/config.py

'''

START MONGODB SERVER

TO INDEX TERMS:

''' bash

cd mybackend/
python2 index.py
python2 search.py

'''

RUN SERVER :

''' bash

cd back to search #projectfolder
python2 manage.py runserver

'''

TEST

''' bash 
cd mybackend/ 
python2 tests.py

'''

