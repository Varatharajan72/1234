N,M=map(int,input().split())
def lcm(N,M):
   if  N>M:
       z=N
   else:
       z=M

   while(True):
       if((z%N==0) and (z% M==0)):
           lcm=z
           break
       z+=1

   return lcm


print(lcm(N,M))
