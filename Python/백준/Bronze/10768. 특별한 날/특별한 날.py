m = int(input())
d = int(input())
if m<2:
  print("Before")
elif m==2:
  print("After" if d>18 else "Before" if d<18 else "Special")
else:
  print("After")