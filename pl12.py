N,K=map(int,input().split())
p=list(map(int,input().split()[:N]))
for i in range(K):
    p=[p[-1]]+p[:-1]
print(*p,end=" ")
