import os
from datetime import datetime

#https://www.youtube.com/watch?v=tJxcKyFMTGo

#print(dir(os))

os.chdir('C:\\Users\\qinlo\\OneDrive\\Desktop')

#os.mkdir('FROM_PY')
#os.mkdirs('OS-Demo-2/Sub_Dir-1')
#os.rmdir('FROM_PY')
#os.removedir('FROM_PY')
# os.rename('New Text Document.txt','temp.txt')
#print(os.getcwd())
#print(os.listdir())
# mod_time = os.stat('temp.txt').st_ctime
# print(datetime.fromtimestamp(mod_time))

# for dirpath,dirnames,filenames in os.walk('C:\\Users\\qinlo\\OneDrive\\Desktop\\JOB'):
#     print('Current Path:',dirpath)
#     print('Directories',dirnames)
#     print('Files',filenames)
#     print()

print(os.environ.get('USERPROFILE'))

file_path = os.path.join(os.environ.get('USERPROFILE'),'temp.txt')
print(file_path)

# with open(file_path,'w') as f:

print(os.path.exists('/tmp/temp.txt'))  #  basename   dirname

os.path.isdir('tem/temp.txt')    # isfile    
 #  splittext the file root and extension

print(dir(os.path))