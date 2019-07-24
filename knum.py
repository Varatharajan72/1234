N,K=map(int,input().split())
n=list(map(int,input().split()[:N]))
z=[]
for k in n:
   if(k<=k+1):
     z.append(k)
print(z[K-1])  
  
