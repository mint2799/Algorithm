stroke = {'j':2, 'o':1, 'i':2}
cnt = 0
n = int(input())
s = input()
for i in s:
    cnt += stroke[i]
print(cnt)