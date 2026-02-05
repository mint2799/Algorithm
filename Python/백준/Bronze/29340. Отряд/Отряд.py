a = input()
b = input()
print(''.join(str(max(x, y)) for x,y in zip(a, b)))