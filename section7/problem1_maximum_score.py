n, m = map(int, input().split()) # reading N and M from user input
problems = [] # initializing an empty list to store problem details
for i in range(n):
    score, time = map(int, input().split())
    problems.append((score, time)) # adding a tuple of score and time to the problems list

# sorting the problems list in descending order of score per unit time
problems.sort(key=lambda x: x[0]/x[1], reverse=True)

max_score = 0 # initializing maximum score to 0
for score, time in problems:
    if m >= time: # if there is enough time to solve the problem
        max_score += score
        m -= time # reducing the remaining time

print(max_score) # printing the maximum score
'''
#최대점수를 탐색하기 위한 DFS 
def DFS(L, tot, time):
    global res
    #주어진 제한시간보다 시간의 합이 많을때
    if time > m:
        return
    if L == n:
        #모든 수업을 탐색한 경우
        if tot > res:
            res = tot
    else:
        DFS(L+1, tot + score[L], time + hour[L])
        DFS(L+1, tot, time)
        
    



if __name__ == "__main__":
    #문제의 개수와 제한 시간을 입력 
    n, m = map(int, input().split())
    score = list()
    hour = list()
    
    #각 문제의 점수와 소비 시간을 두 리스트에 저장
    for i in range(n):
        a, b = map(int, input().split())
        score.append(a)
        hour.append(b)
    res=-214700000
    DFS(0,0,0)
    print(res)
'''

#DFS 풀이 2
'''
n, m = map(int, input().split()) # reading N and M from user input
problems = [] # initializing an empty list to store problem details
for i in range(n):
    score, time = map(int, input().split())
    problems.append((score, time)) # adding a tuple of score and time to the problems list

max_score = 0 # initializing maximum score to 0
visited = [False] * n # initializing visited list to keep track of visited problems

def dfs(current_score, current_time):
    global max_score
    if current_time > m: # if we have exceeded the time limit, return
        return
    max_score = max(max_score, current_score) # update maximum score
    for i in range(n):
        if not visited[i]: # if the problem is not visited
            visited[i] = True
            dfs(current_score + problems[i][0], current_time + problems[i][1]) # recursively call dfs with updated score and time
            visited[i] = False # backtrack by unmarking the problem as visited

# call dfs with initial score and time 0
dfs(0, 0)

print(max_score) # printing the maximum score
'''

