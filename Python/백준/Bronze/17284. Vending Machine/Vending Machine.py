buttons = {1:-500, 2:-800, 3:-1000}
b = map(int,input().split())
print(5000+sum(buttons[i] for i in b))