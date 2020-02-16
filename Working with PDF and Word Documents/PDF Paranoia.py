
import os,PyPDF2,sys,re


os.chdir("C:\\Python\\Udemy\\Assignment\\PDFSS")
path = os.getcwd()

for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith('.pdf'):
            pdf = open(os.path.join(folder, file), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdf)
            pdfWriter = PyPDF2.PdfFileWriter()
            pdfWriter.encrypt(sys.argv[1])
            
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
    
            name = os.path.splitext(file)[0]
            newPdf = open(os.path.join(folder, name + '_encrypted.pdf'), 'wb')
            pdfWriter.write(newPdf)
            pdf.close()
            newPdf.close()

print("Encryption Done")



for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith('encrypted.pdf'):
            pdf = open(os.path.join(folder, file), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdf)
            try:
                pageObj = pdfReader.getPage(0)
            except PyPDF2.utils.PdfReadError:
                name = re.sub('_encrypted.pdf', '', file)
                os.remove(os.path.join(folder, name + '.pdf'))

print('Deleted the Original!!')
