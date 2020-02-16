import requests, sys, webbrowser, bs4,os

os.makedirs('Images_Now', exist_ok=True)

print('Searching...')

#res = requests.get('https://gratisography.com/?s='+' '.join(sys.argv[1:]))
#print('https://gratisography.com/?s='+' '.join(sys.argv[1:]))
res = requests.get('https://gratisography.com/?s=dog')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.find_all("img")


for i in range(len(linkElems)):
    try:
        #urlToOpen = 'https://gratisography.com' + linkElems[i].get('src')
        urlToOpen =  linkElems[i].get('src')
        #urlToOpen = 'https://' + linkElems[i].get('src')
    
        #webbrowser.open(urlToOpen)
        res1 = requests.get(urlToOpen)
        res1.raise_for_status()
        imageFile = open(os.path.join('Images_Now',str(i+1)),'wb')
        for chunk in res1.iter_content(100000):
            imageFile.write(chunk)
        
        imageFile.close()

    except:
        print("Some Ref Problem")
        

        
    


print("Copying Done")
