N=int(input())
for n in range (10000):
  if (N==2**n):
    print("yes")
    break
else:
  print("no")
