import sys

s=[]
I = ['1','2','3','4','5','6','7','8']
l= ['a','b','c','d','e','f','g','h']
for i in I:
    for j in l:
        s.append(i+j)

#print(s)
#print(len(s))

def isValidChessBoard(Chess):
    for i in Chess.keys():
        if i in s:
            continue
        else:
            print("Invalid Board, Wrong x-y Axis")
            sys.exit(0)
        
    b=0
    w=0
    for i in Chess.values():
        if i[0]=='b':
            b+=1
        elif i[0]=='w':
            w+=1
        else:
            print("Invalid Board, Wrong initials,i.e. w&b")
            sys.exit(0)
    
        
    countbking = list(Chess.values()).count('bking')
    countwking = list(Chess.values()).count('wking')
    countbpawn = list(Chess.values()).count('bpawn')
    countwpawn = list(Chess.values()).count('wpawn')
    
    if countbking>1 or countwking>1 or countbpawn>8 or countwpawn>8:
        print("Invalid Board, Wrong Count of Characters")
    else:
        if b>16 or w>16:
            print("Invalid Board, More than 16 for Easch Player")
        else:
            print("Congrats!! It is a Valid Board")
        
         
a={'1h': 'bking','3h': 'bpawn', '4c': 'wqueen', '2g': 'bbishop', '5e': 'bqueen', '3e': 'wking'}
isValidChessBoard(a)

##Extra Conditions can be Incorporated in the same code##            
        
            
    
