w = input().upper()
w_list = list(set(w))
res = []
for i in w_list:
  res.append(w.count(i))
print("?" if res.count(max(res)) > 1 else w_list[res.index(max(res))])