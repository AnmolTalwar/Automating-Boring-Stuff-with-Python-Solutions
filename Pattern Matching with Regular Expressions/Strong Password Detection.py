import re
import pyperclip
import sys


Reg1 = re.compile(r'.{8,}')
Reg2 = re.compile(r'[A-Z]+')
Reg3 = re.compile(r'[a-z]+')
Reg4 = re.compile(r'[0-9]+')

text=pyperclip.paste()

y=Reg1.findall(text)
z=Reg2.findall(text)
a=Reg3.findall(text)
b=Reg4.findall(text)

if len(y)==0:
    print("Password is less than 8 Characters")
    sys.exit(0)

elif len(z)==0:
    print("Password has no UpperCase letters")
    sys.exit(0)
          
elif len(a)==0:
    print("Password has no LowerCase letters")
    sys.exit(0)
          
elif len(b)==0:
    print("Password has no digits")
    sys.exit(0)

else:
    print("Correct Password")





