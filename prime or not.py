number=int(input())
if number>1:
   for k in range(2,number):
      if number%k==0:
         print("no")
         break
   else:
        print("yes")
else:
  print("no")
