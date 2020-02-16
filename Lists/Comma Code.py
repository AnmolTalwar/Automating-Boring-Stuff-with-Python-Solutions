def ListtoString(l):
    z=[]
    x=[]
    for i in range(len(l)-1):
        z.append(l[i])
    #print(z)

    x.append('and')
    x.append(l[-1])
    #print(x)

    a= ','.join(z)
    b= ' '.join(x)
    c = a+ " " +b
    print(c)

    
lst = []   
n = int(input("Enter number of elements in your list : "))
for i in range(0, n): 
    ele = input() 
    lst.append(ele) 
      
ListtoString(lst)
    
        
    
