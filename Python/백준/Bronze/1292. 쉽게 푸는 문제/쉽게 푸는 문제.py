a,b = map(int,input().split())
seq = [i for i in range(1,b+1) for j in range(i)]
print(sum(seq[a-1:b]))