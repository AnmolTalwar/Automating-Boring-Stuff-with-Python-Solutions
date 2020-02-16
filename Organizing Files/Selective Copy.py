import re
import os
import shutil

a = input("Please Enter what type of File to copy:\n")

regex = re.compile('^.*\.%s$'%a)


for folderName, subfolders, filenames in os.walk('C:\\MA'):
    for filename in filenames:
        if regex.search(filename):
            print(filename+ " is being copied.")
            path = folderName+"\\"+filename
            shutil.copy(path, "C:\\ATT")
