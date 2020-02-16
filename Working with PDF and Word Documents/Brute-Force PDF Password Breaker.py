
import os,PyPDF2,sys,re,time


os.chdir("C:\\Python\\Udemy\\Assignment\\Brute_Force")
path = os.getcwd()

words = open('words.txt')
list = words.readlines()

print("Decrypting the PDF/PDFs...This may take While!!")
time.sleep(3)
   
for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith('.pdf'):
            pdf = open(os.path.join(folder, file), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdf)

            for name in list:
                password = re.sub("\n","",name)
                if pdfReader.decrypt(password) == 1:
                    print("Unlocked!!")
                    time.sleep(2)
                    print("The Password for %s is: %s"%(file,password))
                    break
                elif pdfReader.decrypt(password.upper()) == 1:
                    print("Unlocked!!")
                    time.sleep(2)
                    print("The Password for %s is: %s"%(file,password.upper()))
                    break
                else:
                    print("Password %s failed" %password)
                    continue
                
