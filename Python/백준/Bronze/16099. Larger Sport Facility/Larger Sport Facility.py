for _ in range(int(input())):
  lt, wt, le, we = map(int,input().split())
  T = lt*wt;  E = le*we
  print("TelecomParisTech" if T>E else "Eurecom" if E>T else "Tie")