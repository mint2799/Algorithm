sides = sorted(list(map(int,input().split())))
if (sides[0]+sides[1] > sides[2]) and (sides[2]**2 == sides[0]**2 + sides[1]**2): print(1)
elif (sides[0]+sides[1] > sides[2]) and (sides[0]==sides[1]==sides[2]): print(2)
else: print(0)