x,y,z=input().split()
if(x>=y) and (x>=z):
  lar=x
elif(y>=x) and (y>=z):
  lar=y
else:
  lar=z
print(lar)
