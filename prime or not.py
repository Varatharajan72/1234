N=int(input())
if N>1:
   for k in range(2,N):
      if N%k==0:
         print("no")
         break
   else:
        print("yes")
else:
  print("no")
