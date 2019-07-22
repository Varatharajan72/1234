N=int(input())
if N>1:
   for m in range(2,N):
      if N%m==0:
         print("no")
         break
   else:
        print("yes")
else:
  print("no")                 
