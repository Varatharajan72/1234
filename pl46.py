import math
A=int(input())
b=math.radians(A)
c=math.sin(b)
if(b<1):
    print(int(round(c,1)))
elif(b>1):
    print(round(c))
    
