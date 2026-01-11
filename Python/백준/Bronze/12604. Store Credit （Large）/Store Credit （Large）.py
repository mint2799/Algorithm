for i in range(int(input())):
    c = int(input())
    I = int(input())
    p = list(map(int, input().split()))

    seen = {}
    for idx, price in enumerate(p):
        need = c - price
        if need in seen:
            print(f"Case #{i+1}: {seen[need]+1} {idx+1}")
            break
        seen[price] = idx