def NBottlesofBeer(n):
  k = n
  while n > 0:
    bottle = "bottles" if n > 1 else "bottle"
    nextBottle = "no more bottles" if n == 1 else f"{n - 1} bottle{'s' if n-1!=1 else ''}"
    print(f'{n} {bottle} of beer on the wall, {n} {bottle} of beer.\nTake one down and pass it around, {nextBottle} of beer on the wall.\n')
    n -= 1
  print(f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {k} bottle{'s' if k!=1 else ''} of beer on the wall.")
NBottlesofBeer(int(input()))