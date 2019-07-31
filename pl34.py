S=str(input())
u=[]
for i in range(0,len(S),3):
  u.append(S[i])
print(*u,sep="")
