
N,K=input().split()
for i in range (int(K)):
  N=N[-1]+N[:-1]
print(N,end='')
