import re
import os
import shutil

a = input("Please Enter what type of File to copy:\n")
b = input("Please Enter the Base Name of the series file:\n")
c=input("Input the full directory path you want to check for file sequence:\n")
os.chdir(c)
path1 = os.getcwd()

regex = re.compile('(^(%s)(\d{1,})\.%s$)'%(b,a))

e = []
for folderName, subfolders, filenames in os.walk(path1):
    for filename in filenames:
        if regex.search(filename):
            d=regex.findall(filename)
            e.append(int(d[0][2]))
            x=len(d[0][2])
        else:
            #print("Either the File name or the directory name is wrong. There might be a possibility that the directory doesnot contain the asked files")
            continue
w=0
#print(e)
for i in range(len(e)-1):
    if e[i]!=e[i+1]-1:
        w = e[i+1]
        print("There is a flaw in the sequence at "+str(w))
        print("Renaming the Sequence.")
        break
    else:
        continue


if w==0:
    print("The Sequence is perfectly fine!")
else:
    i = 1
    for file in os.listdir():
        mo = regex.search(file)
        if mo:
            old_name = os.path.abspath(file)
            new_suffix = mo.group(2) + str(i).zfill(x) +"."+a
            new_name = os.path.join(path1, new_suffix)
            i += 1
            print('Renaming: %s to %s' % (old_name, new_name))
            shutil.move(old_name, new_name)
        else:
            print("No match found!")
    
    
            
