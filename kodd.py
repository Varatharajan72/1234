N,K=map(int,input().split())
n=list(map(int,input().split()[:N]))
z=[]
for k in n:
   if(k%2!=0):
     z.append(k)
print(z[K-1])  

