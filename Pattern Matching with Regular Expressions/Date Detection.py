import re
import pyperclip
import sys

Dateregex = re.compile(r'((\d\d)\/(\d\d)\/(\d\d\d\d))')

text=pyperclip.paste()

try:
    Phone = Dateregex.findall(text)
    day = Phone[0][1]
    month = Phone[0][2]
    year = Phone[0][3]

except:
    print("Please enter Date in dd/mm/yyyy format")
    

if month=='04'or month=='06'or month=='09'or month=='11' and int(day)>31:
    print("Wrong Date in the Input")
    sys.exit(0)

elif month=='02' and int(day)>29:
    print("Wrong Date in the Input, Problem with Feb,i.e. more than 29 Days")
    sys.exit(0)

elif bool(int(year)%100):
    if bool(int(year)%4):
        if month=='02' and int(day)>28:
            print("wrong Date as Feb in Non-Leap Year cannot have more than 28 Days")
            sys.exit(0)
        else:
            print("Correct Date")
    else:
        print("Correct Date")      

else :
    print("Correct Date")
        
    
    
