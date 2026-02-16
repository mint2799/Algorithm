c = {'a': 4, 'e': 3, 'i': 1, 'o': 0, 's': 5}
w = input()
print(''.join(str(c.get(i, i)) for i in w))