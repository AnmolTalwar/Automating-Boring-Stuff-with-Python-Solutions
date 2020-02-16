import requests, bs4,time,datetime
from twilio.rest import Client

accountSID = 'ACabe015023240359671166f9226420fd6'
authToken  = '955698662159574d7c51e0bcdd6d410e'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+12029315408'
myCellPhone = '+919035163480'


def CheckForRain():
    res = requests.get('https://forecast.weather.gov/MapClick.php?lat=36.37410569300005&lon=-119.27022999999997#.XjQtpEczZPY')
    res.raise_for_status()

    Soup = bs4.BeautifulSoup(res.text, 'html.parser')
    Check = Soup.find('li',class_='forecast-tombstone')
    Check1 = Check.text.lower()

    if ("rain" in Check1) or ("cloudy" in Check1):
        message = twilioCli.messages.create(body='Reminder!! Carry an Umbrella. It might Rain Today in California!!', from_=myTwilioNumber, to=myCellPhone)
    else:
        print("No need for a Reminder!!")

    time.sleep(86400)
    CheckForRain()



tommorow = datetime.datetime(2020,2,1,5,30)

while datetime.datetime.now()< tommorow:
    time.sleep(1)
    
CheckForRain()
    
        
        
    

    
