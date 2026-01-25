T = int(input())
for _ in range(T):
  loop, word = map(str, input().split())
  loop = int(loop)
  word = list(word)
  for w in word:
    for i in range(loop):
      print(w, end ='')
  print()  