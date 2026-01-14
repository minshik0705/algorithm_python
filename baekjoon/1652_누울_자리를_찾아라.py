N = int(input())
room = [list(input().rstrip()) for _ in range(N)]
result = [0,0]
for i in range(N):
  len_row, len_col = 0,0
  for j in range(N):
    #가로의 길이부터 확인
    if room[i][j] == '.':
      len_row +=1
    else:
      len_row = 0
    if len_row == 2:
      result[0] += 1
      
    if room [j][i] =='.':
      len_col +=1
    else:
      len_col = 0
    if len_col == 2:
      result[1] += 1
print(*result)