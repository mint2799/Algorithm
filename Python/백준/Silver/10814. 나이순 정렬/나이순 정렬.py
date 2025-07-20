member = [input().split() for _ in range(int(input()))]
member.sort(key = lambda x:int(x[0]))
for a,n in member: print(a,n)