s = input().split()
ign = {'i','pa','te','ni','niti','a','ali','nego','no','ili'}
res = [ word[0].upper() for idx, word in enumerate(s) if idx == 0 or word not in ign]
print(''.join(res))