N,M=map(int,input().split())
def HCF(N,M):
    if N<M:
        smaller=N
    else:
        smaller=M
    for k in range(1, smaller+1):
        if((N%k==0) and (M%k==0)):
            HCF=k
            
    return HCF
print(HCF(N,M))                                       
