import webbrowser,pyautogui,time,os,sys,re

os.chdir("C:\\Python\\Udemy\\Assignment\\Hangout")
pyautogui.PAUSE = 0.5

message = sys.argv[1]

print("Please Enter the correct email address or the name of the person you want to send the message to in \"List.txt\" file. If not entered, Press \"Ctrl+C\" to Break the Script")
print("Waiting for 5 Seconds!!")
time.sleep(5)

Read = open("List.txt")
List = Read.readlines()
names = []

for name in List:
    names.append(re.sub("\n","",name))

    

webbrowser.open('https://hangouts.google.com/')

time.sleep(5)

while pyautogui.locateOnScreen('New.png') is None:
    time.sleep(5)


for email in names:
    pyautogui.moveTo(1091,581)
    pyautogui.click()
    pyautogui.typewrite(email)
    time.sleep(2)
    pyautogui.moveTo(295,429)
    pyautogui.click()
    time.sleep(2)
    print("Sending Message to: %s"%email)
    pyautogui.typewrite(message)
    pyautogui.press('enter')


print("Sent Messages to all!!")
