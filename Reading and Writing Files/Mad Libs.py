import pyinputplus as py
import re


File = open('Anmol.txt','r')
Text = File.read()
print(Text)

AdjReg = re.compile('ADJECTIVE')
NounReg = re.compile('NOUN')
Verbreg = re.compile('VERB')



while AdjReg.search(Text) is not None:
    Adjective=py.inputStr("Please Enter an Adjective:\n")
    Text = AdjReg.sub(Adjective,Text,1)
    

while NounReg.search(Text) is not None:
    NOUN=py.inputStr("Please Enter an NOUN:\n")
    Text = NounReg.sub(NOUN,Text,1)


while Verbreg.search(Text) is not None:
    VERB=py.inputStr("Please Enter an VERB:\n")
    Text = Verbreg.sub(VERB,Text,1)



print(Text)

n_File = open('Talwar.txt', 'w')
n_File.write(Text)

File.close()
n_File.close()
