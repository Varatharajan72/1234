p=int(input())
q=0
r=1
n=1
for i in range(p):
	print(n,end=' ')
	n=q+r
	q=r
	r=n          
