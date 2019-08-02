N,K=map(int,input().split())
s=0
while (N>2):
  if (N%K!=0):
    s+=1
  N/=K
if (s==0):
  print("yes")  
else:
  print("no")
