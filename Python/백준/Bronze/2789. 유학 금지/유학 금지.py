s = input()
words = ['C','A','M','B','R','I','D','G','E']
print(''.join(w for w in s if w not in words))