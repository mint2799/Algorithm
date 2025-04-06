name = [input() for _ in range(int(input()))]
new_name = sum(1 for n in name if n.startswith('C'))
print(new_name)