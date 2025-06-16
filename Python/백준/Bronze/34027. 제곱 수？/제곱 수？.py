for _ in range(int(input())):
    n = int(input())
    root = int(n ** 0.5)
    print("1" if root * root == n else "0")