S=str(input())
p=0
for k in S:
    if S.count(k)>p:
        p=S.count(k)
        q=k
print(q)
