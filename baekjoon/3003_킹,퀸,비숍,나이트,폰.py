full = [1,1,2,2,2,8]
pieces = list(map(int,input().split()))
answer = [a-b for a, b in zip(full,pieces)]
for element in answer:
  print(element, end = ' ')