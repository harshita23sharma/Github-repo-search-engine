import os
print(os.getcwd()[1])
# FOLDER_PATH = ' /home/infoobjects/Desktop'
FOLDER_PATH = os.getcwd()
INNER_PATH = '/product/templates/product'
TEMPLATES_PATH = FOLDER_PATH + INNER_PATH

# INDEX_NAME = 'bulk_example44'
# INDEX_NAME = 'test_bulk33'
INDEX_NAME = 'test_bulk334'

MATRIX_NAME = 'my_matrix3.dat'
INPUT_FOLDER = '/haproxy'
FILES_COUNT = 106 #NUMBER OF FILES 105 .c FILES IN THE INPUT FOLDER (/haproxy)
WORKING_DIR = '/home/infoobjects/Desktop/search'