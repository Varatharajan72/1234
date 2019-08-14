S=list(input().split()[:2])
a=S[0]
b=S[1]
for k in a:
  if(k in b):
    print("yes")
    break
else:
  print("no")

