
import os
import fnmatch
FOLDER = '/haproxy'
root = os.getcwd() + FOLDER
print(root)
for path, subdirs, files in os.walk(root):
    for name in files:
        # print(name)
        if fnmatch.fnmatch(name, '*.c'):            
            path = os.path.join(path, name)
            # print(name)
            try:

                # f = open(path,'rb') 
                matching = True

                found = []
                with open(path, 'r') as file:
                    it = iter(file)
                    for line in it:
                        # print(line)
                        if matching:
                            if line.strip() == '':
                                break
                            else:
                                found.append(line)
                        elif line.endswith('PATTERN:'):
                            for _ in range(6):
                                next(it)
                            matching = True
                for line in found:
                    print(line)
            except:
                pass

