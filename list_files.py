import os

def list_all_files(rootdir):  
    _files = []  
    list = os.listdir(rootdir) 
    for i in range(0,len(list)):  
        path = os.path.join(rootdir,list[i])  
        if os.path.isdir(path):  
            _files.extend(list_all_files(path))  
        if os.path.isfile(path):  
            _files.append(list[i])  
    return _files 

files_500 = list_all_files('results/500')
files_10 = list_all_files('results/10')

for file in files_500:
    if not file in files_10:
        print(file)
