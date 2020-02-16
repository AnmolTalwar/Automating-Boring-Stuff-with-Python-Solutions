import re
import os
import shutil

a=input("Input the Directory you want to check for file size greater than 0.5Mb\n:")
os.chdir(a)
path1 = os.getcwd()


for folderName, subfolders, filenames in os.walk(path1):
    for filename in filenames:
        path = folderName+"\\"+filename
        if os.path.getsize(path) > 500000:
            print(filename+" with path "+path+ " has size greater than 0.5 Mb")        
