n = input()
print(10+int(n[2:]) if n.startswith('10') else int(n[0])+int(n[1:]))