p=int(input())
q=list(map(int,input().split()[:p]))
r=0
for s in q:
   r+=s 
t=r//p
print(t)          
