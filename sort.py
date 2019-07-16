g=int(input())
h=list(map(int,input().split()[:g]))
h.sort()
for i in h:
    print(i,end=" ")
