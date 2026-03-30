img = [input().split() for _ in range(15)]

if any('w' in row for row in img):
    print("chunbae")
elif any('b' in row for row in img):
    print("nabi")
else:
    print("yeongcheol")