k=input()
c=0
for j in range(len(k)):
    if (k[j].isalpha() or k[j].isnumeric() or k[j]==" "):
      continue
    c=c+1
else:
    print(c)    
