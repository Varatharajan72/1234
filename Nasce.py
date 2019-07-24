N=int(input())
n=list(map(int,input().split()[:N]))
for k in range (len(n)-1):
   if(n[k]>n[k+1]):
      print(k)  
     
