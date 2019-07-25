N,S=map(str,input().split())
if(len(N)!=len(S)):
 print("no")
else:
 p=[N.count(k) for k in N]
 q=[S.count(k) for k in S]
if(p==q):
 print("yes")
else:
 print("no") 
 
