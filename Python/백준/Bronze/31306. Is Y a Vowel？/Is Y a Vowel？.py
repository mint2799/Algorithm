s = input()
vowel = ['a', 'e', 'i', 'o', 'u', 'y']
count_5 = sum(s.count(c) for c in vowel[:5])
count_all = sum(s.count(c) for c in vowel)
print(count_5, count_all)