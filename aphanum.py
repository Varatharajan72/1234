number=list(input())
p=0
q=0
for r in number:
	if r.isalpha():
		p+=1
	elif r.isdigit():
		q+=1
print("Yes" if p and q >0 else "No")                     
