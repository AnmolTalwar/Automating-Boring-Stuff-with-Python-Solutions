

import time,pyperclip

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input()                    
print('Started.')
startTime = time.time()    
lastTime = startTime
lapNum = 1

copy = []
copy.append("LapNum TotalTime LapTime")
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s ( %s)' % (lapNum, str(totalTime).rjust(2), lapTime), end='')
        lapNum += 1
        lastTime = time.time()
        copy.append(" #"+str(lapNum)+"       "+str(totalTime)+"     "+str(lapTime))
        
except KeyboardInterrupt:
    print('\nDone.')


copy1 = '\n'.join(copy)
pyperclip.copy(copy1)

    
       
       
