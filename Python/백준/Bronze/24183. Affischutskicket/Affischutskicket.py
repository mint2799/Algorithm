x,y,z = map(int,input().split())
c4 = 0.229 * 0.324; a3 = 0.297 * 0.420; a4 = 0.210 * 0.297
print(2*c4*x+2*a3*y+a4*z)