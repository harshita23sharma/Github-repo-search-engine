# f = open(file, 'rb')
import os
import fnmatch
FOLDER = '/haproxy'
root = os.getcwd() + FOLDER
print(root)
for path, subdirs, files in os.walk(root):
	for name in files:
		if fnmatch.fnmatch(name, '*.c'):            
			path = os.path.join(path, name)
			print(name)
			try:

				f = open(path,'rb') 

				while(True):
					piece = f.read(1024)  
					if not piece:
						break
					# p = process_data(piece)
					print(piece)
					print(" ")
					print('..................................')
					print(' ')
				f.close()
			except:
				continue