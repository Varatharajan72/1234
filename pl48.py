N=int(input())
a=[]
for i in range (1,N+1):
  if (N%i==0):
    a.append(i)
for k in a:
  if (k%2!=0):
    print (k,end=" ")
    
