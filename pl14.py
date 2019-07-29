N=input()
S=str(input())
for k in S:
    if (k=='a' or k=='e' or k=='i' or k=='o' or k=='u'):
        S=S.replace(k,"")
print(S[::-1]) 
