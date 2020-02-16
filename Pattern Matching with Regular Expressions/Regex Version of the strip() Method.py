import re
import sys


def Strip(string,argument):

    if argument=="" or argument=="None" or argument==None :
        reg1 = re.compile(r'^\s+')
        reg3 = re.compile(r'^\s+$')
        a = reg1.sub("",string)
        print(reg3.sub("",a))

    else:
        reg2 = re.compile(format(argument))
        #print(reg2.findall(string))
        #print(string)
        print(reg2.sub("",string))


Strip("   Hi Anmol   ","")
