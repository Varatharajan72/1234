p,q=list(map(int,input().split()))
r,s=list(map(int,input().split()))
t,u=list(map(int,input().split()))
if(p==r==t) or (q==s==u) or (p==q) or (r==s) or (t==u):
    print("yes")
else:
    print("no")
