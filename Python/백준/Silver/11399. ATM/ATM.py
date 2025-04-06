n = int(input())
p = sorted(list(map(int,input().split())))
time, total = 0, 0
for i in p:
    time += i
    total += time
print(total)