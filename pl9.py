l,r=list(map(int,input().split()))
s=0
for i in range(l,r+1):
    if i>1:
        for x in range(2,i):
            if(i%x==0):
                break
        else:
            s+=1
print(s)
