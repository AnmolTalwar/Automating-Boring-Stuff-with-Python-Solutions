import pyautogui,random,time

move = [(3, 0),(0, 3),(-3, 0),(0, -3)]

try:
    while True:
        time.sleep(10)
        pyautogui.move(random.choice(move), duration=0.25)
        
except:
    print('Script Off')
    
