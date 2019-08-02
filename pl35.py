import string
N=input()
N.split()
N=N.replace(" ","")
b=[i for i in N if N.count(i)==1]
c=' '.join(b)
print(c.lower())
