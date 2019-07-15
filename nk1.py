N,K=map(int,input().split())
arrq=[]
j=N
m=1
arrq=[int(i)for i in input().split()]
sum=0
i=0
while K>0:
  sum+=arrq[i]
  K=K-1
  i=i+1
print(sum)
