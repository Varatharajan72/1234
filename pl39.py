N=int(input())
s=0
while (N>2):
  if (N%2!=0):
    s+=1
  N/=2
if (s==0):
  print("yes")  
else:
  print("no")
