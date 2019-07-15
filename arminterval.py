p,q=map(int,input().split())
for n in range(p,q):
   order = len(str(n))
   sum = 0
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if n == sum:
       print(n,end=" ")
