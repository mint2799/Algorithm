n = int(input().strip())
s = input().strip()
scnt = s.count('s')
tcnt = s.count('t')

idx = 0
while scnt != tcnt:
    if s[idx] == 's':
        scnt -= 1
    else:
        tcnt -= 1
    idx += 1
print(s[idx:])