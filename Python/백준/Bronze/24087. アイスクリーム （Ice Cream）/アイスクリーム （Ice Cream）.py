s = int(input())
a = int(input())
b = int(input())

cost = 250

if s <= a:
    print(cost)
else:
    diff = s - a
    need = (diff + b - 1) // b
    cost += need * 100
    print(cost)
