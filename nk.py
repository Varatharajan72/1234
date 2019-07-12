N,K=map(int,input().split())
arrq=[]
k=N
m=1
while N>0:
  arrq.append(m)
  N=N-1
  m=m+1
print(arrq)
sum=0
i=0
while K>0:
  sum+=arrq[i]
  K=K-1
  i+=1
print(sum) 
