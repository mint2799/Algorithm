code = input()[:5]
subj = [s for _ in range(int(input())) if (s := input())[:5] == code]
print(len(subj))