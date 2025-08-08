h = int(input())
print(1 if h==0 else 0 if h==1 else ('4' if h%2 else '')+'8'*(h//2))