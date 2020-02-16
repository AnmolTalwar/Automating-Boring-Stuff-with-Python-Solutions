import numpy as np
import pandas as pd

z=0
def collatz(number):
    if number%2==0:
        z = number/2
        #return  z
        print(z)
    else:
        z = 3*number+1
        #return z
        print (z)
    if z==1:
        print("Done!")
    else :
        collatz(z)
        

print("Input an integer")
try:
    x= int(input())
except:
    print("Enter an Integer")
    
collatz(x)



        
    
