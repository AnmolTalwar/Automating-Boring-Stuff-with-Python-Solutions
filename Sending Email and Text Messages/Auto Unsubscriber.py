import webbrowser,imapclient,pyzmail,bs4

password=input("Enter your PASSWORD:\n")

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login("anmol.talwar93@gmail,com", password)

imapObj.select_folder('INBOX', readonly=True)
UDSs = imapObj.search(['BODY unsubscribe', 'SINCE 01-Jan-2020'])
rawMessages = imapObj.fetch(UDSs, ['BODY[]'])

for id in UDSs:
    
    message = pyzmail.PyzMessage.factory(rawMessages[id][b'BODY[]'])
    
    try:
        html_obj = message.html_part.get_payload().decode(message.html_part.charset)
        
        soup = bs4.BeautifulSoup(html_obj, "html.parser")
        elem = soup.select('a')
        
        for i in range(len(elem)):
            url = elem[i].get('href')
            if 'unsubscribe' in url:
                webbrowser.open(url)
                
    except:
        print('Problem with Reference Link')
        
imapObj.logout()
