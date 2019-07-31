N,K=map(int,input().split())
S=map(int,input().split()[:N])
for k in S:
    if (k==K):
        print("Yes")
        break
else:
    print("No")
    
