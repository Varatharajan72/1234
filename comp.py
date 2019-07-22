N=int(input())
p=0
if(N>2):
    for k in range(2,int(N/2)+1):
        if N%k==0:
            print("yes")
            p=1
            break
if p==0 or p==2:
    print("no")            
