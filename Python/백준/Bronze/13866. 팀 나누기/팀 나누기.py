abcd = list(map(int,input().split()))
print(abs(sum(abcd) - 2*(min(abcd)+max(abcd))))