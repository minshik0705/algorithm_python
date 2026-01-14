N = int(input())
score = list(map(int, input().split(' ',N)))
score.sort(reverse = True)
max = score[0]
for i in range(N):
  score[i] = (score[i]/max)*100
print(sum(score)/N)