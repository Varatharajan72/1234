g=int(input())
h=list(map(int,input().split()[:g]))
h=list(sorted(h))
print(*h)      
