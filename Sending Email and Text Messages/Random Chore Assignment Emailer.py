import smtplib, re, os, random

os.chdir("C:\\Python\\Udemy\\Assignment\\Email_List")

smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
smtpObj.ehlo()
smtpObj.starttls()

password = input("Enter your PASSWORD:\n")
smtpObj.login('anmol.talwar93@gmail.com', password)



chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

file = open("List.txt",'r')
List = file.readlines()
emails=[]

for names in List:
    emails.append(re.sub("\n","",names))
    

for email in emails:
    randomChore = random.choice(chores)
    chores.remove(randomChore)
    body = "Subject: Chores For The Week.\nHello Dear,\n\nThe work for you this week is %s"%randomChore
    print('Sending email to %s...' % email)
    sendmailStatus = smtpObj.sendmail('anmol.talwar93@gmail.com',email,body)

    if sendmailStatus != {}:
           print('There was a problem sending email to %s: %s' % (email,sendmailStatus))

smtpObj.quit()
           
