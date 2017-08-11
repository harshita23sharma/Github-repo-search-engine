index.py :  index all the data of the github repository in raw form

search.py : Picks up data from mongodb and prepare hashed dictionary of all corpus. Also forms pandas arrays to store all corpus along with their frequencies and scores.Scoring is done to priortize the relevant search results. Data is properly indexed in mongodb and stored in matrices in pickle form for fast search querying.

load_search.py : loads the previously pickled pandas array and does scoring of the queried keyword.

tests.py : tests for queried keyword and most relevant file as output