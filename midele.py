S=input()
n=len(S)
if n%2!=0:
    S=S[:int(n/2)]+'*'+S[int(n/2)+1:n]
else:
    S=S[:int(n/2)-1]+'**'+S[int(n/2)+1:n]
print(S)
