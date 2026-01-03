#include <string.h>
word = str(input())
word = word.upper()
alphabet = set(word)
result = []
for i in alphabet:
  result.append((i, word.count(i)))
result.sort(key = lambda x : -x[1])
if len(result) == 1:
  print(result[0][0])
elif result[0][1] == result[1][1]:
  print('?')
else:
  print(result[0][0])