
s=input().split()
p=s[0]
q=s[1]
count=0
i=0
while(i<len(p) and count<2):
    if(p[i]!=q[i]):
        count+=1
    i+=1
if(count==1 or count==0):
    print("yes")
else:
    print("no")
