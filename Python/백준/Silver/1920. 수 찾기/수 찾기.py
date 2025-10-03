import sys

N = int(input())
A = set(list(map(int, sys.stdin.readline().split())))
M = int(input())
M_num = list(map(int, sys.stdin.readline().split()))

for num in M_num:
    print("1") if num in A else print("0")