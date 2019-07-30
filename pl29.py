import math
i,r=list(map(int,input().split()))
count=0
for k in range (i,r+1):
  j=k**0.5
  if (j-math.floor(j)==0) :
    count+=1
print(count)
