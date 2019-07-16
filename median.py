import statistics
g=int(input())
h=list(map(int,input().split()[:g]))
print(statistics.median(h))         
