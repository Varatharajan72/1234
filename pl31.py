S=input()
sum=0
for k in range (0,len(S)):
    if(S[k]=="("):
        sum+=1
    elif(S[k]==")"):
        sum-=1
if sum==0: 
    print("yes")
else:
    print('no')
