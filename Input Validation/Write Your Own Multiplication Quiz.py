import pyinputplus as py
import random,time

nQuestions=10
Ncorrect=0

for Qnumber in range(nQuestions):
    num1=random.randint(0,9)
    num2=random.randint(0,9)

    prompt = '#%s:%s x %s = '%(Qnumber,num1,num2)

    try:
        Check=py.inputStr(prompt, allowRegexes=['^%s$'%(num1*num2)],
                  blockRegexes=['.*','Incorrect!'],timeout=8,limit=3)
    


    except py.TimeoutException:
        print("Time Lapsed!")
    except py.RetryLimitException:
        print("No More Tries!")
    else:
        print("Correct")
        Ncorrect+=1
    time.sleep(1)

print("Your Total Score out of 10: "+str(Ncorrect))
    



