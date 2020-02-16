import requests, sys, webbrowser, bs4,os,time

res = requests.get('https://economictimes.indiatimes.com/')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.find_all("a")
print("Total of " +str(len(linkElems))+" links present in economictimes.indiatimes.com")
time.sleep(2)
print("")
print("")

for i in range(len(linkElems)):
    Check=[]
    try:
        for j in range(0,4):
            Check.append(linkElems[i].get('href')[j])
        if ''.join(Check)=="http":
            urlToOpen = linkElems[i].get('href')
        else:
            urlToOpen = 'https://economictimes.indiatimes.com/' + linkElems[i].get('href')
            
        res1 = requests.get(urlToOpen)
        if res1.status_code == 404:
            print("404 error for: "+urlToOpen)
        else :
            print("Working fine! : "+urlToOpen)

    except:
        print("Reference Problem or Missing Schema with: "+ urlToOpen )
        continue
        

        
print("Page Checked Fully for URLs!!")
