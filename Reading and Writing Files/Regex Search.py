import re
from pathlib import Path

p = Path('C:\\Python\\Udemy\\Assignment\\Confidential')
a = input("Please Enter something you want to Search:\n")
regex=re.compile('%s'%a)


for textFilePathObj in p.glob('*.txt'):
    Counter = 0
    #print(textFilePathObj.name)
    File=open('C:\\Python\\Udemy\\Assignment\\Confidential\\%s'%textFilePathObj.name,'r')
    Text = File.read()
    #print(Text)
    
    for i in regex.findall(Text):
        Counter+=1
    print("%s has "%textFilePathObj.name+ str(Counter)+ " Occurances of what you are searching!!")
    File.close()   
     
     
