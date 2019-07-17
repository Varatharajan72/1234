p=input()
q=p.strip()
r=1
for j in range (len(q)):
    if(q[j]==' ' and (q[j]!=q[j+1])):
        r=r+1
if(r>1):
    print(r)         
