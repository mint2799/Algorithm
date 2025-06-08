ca,ba,pa = map(int,input().split())
cr,br,pr = map(int,input().split())
c = cr-ca if cr>ca else 0
b = br-ba if br>ba else 0
p = pr-pa if pr>pa else 0
print(c+b+p)