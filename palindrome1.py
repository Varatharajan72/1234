z=int(input())
temper=z
rever=0
while(z>0):
    dig=z%10
    rever=rever*10+dig
    z=z//10
if(temper==rever):
    print("yes")
else:
    print("no")
