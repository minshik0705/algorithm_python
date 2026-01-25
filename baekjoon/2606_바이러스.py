numCom = int(input()) #number of computers  #컴퓨터의 수
numCon = int(input()) #number of connections#네트워크 연결 수

graph = [[] for _ in range(numCom+1)]

for i in range(numCon):
  a, b = map(int,input().split())
  #양방향 그래프 표현하기
  graph[a].append(b)
  graph[b].append(a)
visited = [False] * (numCom+1)
count = -1

def DFS(v):
  visited[v] = True
  global count
  count += 1
  for i in graph[v]:
    if not visited[i]:
      DFS(i)

DFS(1)
print(count)