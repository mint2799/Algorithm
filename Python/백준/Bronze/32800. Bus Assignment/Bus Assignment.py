people = max_people = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    people += b - a
    max_people = max(max_people, people)
print(max_people)