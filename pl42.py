n=int(input())
N=list(map(int,input().split()[:n]))
a=[]
for i in sorted(N):
  a.append(i)
if(a==N):
  print("yes")
else:
    print("no")
    
