p=input()
q=p.lstrip('-').replace('.','',1).isdigit()
if(q==True):
	print("yes")
else:
	print("No")
