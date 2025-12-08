n = int(input())
s = input()
print(s[:n-1] if s[n-1] == 'G' else s+'G')