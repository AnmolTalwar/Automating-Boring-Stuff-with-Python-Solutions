
import requests, os, bs4

os.chdir("C:\\Python\\Udemy\\Assignment")
os.makedirs('xkcd', exist_ok=True)

num = 2261


def downloadXkcd():
    global num
    
    try:
        print('Downloading page https://xkcd.com/%s...' % (num))
        res = requests.get('https://xkcd.com/%s' % (num))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

          
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
         else:
            comicUrl = comicElem[0].get('src')
              
            print('Downloading image %s...' % (comicUrl))
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

              
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
                imageFile.close()

        num+=1
        downloadXkcd()

        except requests.exceptions.HTTPError:
            print("No New Comic was found!! Will try again in 24 hours")
            for i in range(86400):
                time.sleep(1)
            downloadXkcd()



downloadXkcd()            
          
    
        
    


