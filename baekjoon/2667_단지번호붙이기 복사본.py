N = int(input())
M = [list(map(int, input())) for _ in range(N)]
num = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def DFS(x,y):
  if x<0 or x>=N or y<0 or y>=N:
    return False  #탐색을 끝내야하는 경우
  if M[x][y] == 1:
    global count
    count +=1
    M[x][y]=0 #이미 탐색을 한 곳은 재탐색하지 않아야 한다
    for i in range(4):
      nx = x +dx[i]
      ny = y +dy[i]
      DFS(nx,ny)
    return True #계속 탐색을 해도 되는 경우
  return False

count = 0 
result = 0

for i in range(N):
  for j in range(N):
    if DFS(i,j) == True:
      num.append(count)
      result +=1
      count = 0
num.sort()
print(result)
for i in range(len(num)):
  print(num[i])

