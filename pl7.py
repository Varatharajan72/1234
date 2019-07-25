N=list(input())
for k in range (0,(len(N)-1),2):
  t=N[k+1]
  N[k+1]=N[k]
  N[k]=t
print("".join(N)) 

