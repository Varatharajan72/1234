A,B,C=map(int,input().split())
if(A==0 or B==0 or C==0):
  print("no")
elif ((A>0 and A<180) or (B>0 and B<180) or (C>0 and C<180)):
  s=A+B+C
  if (s==180):
    print("yes")
  else:
    print("no")
   
