a = int(input())
b = int(input())
s = (a + b) % 12
print(12 if s == 0 else s)