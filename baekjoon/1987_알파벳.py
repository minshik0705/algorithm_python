import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

arr = [[ord(ch) - 65 for ch in row] for row in board]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

start_mask = 1 << arr[0][0]

# 상태 key를 정수로 인코딩:
# x, y는 0~19 => 각각 5비트씩, 총 10비트 사용 가능
# key = (mask << 10) | (x << 5) | y
def make_key(x, y, mask):
    return (mask << 10) | (x << 5) | y

ans = 1

stack = [(0, 0, start_mask, 1)]
seen = set()
seen.add(make_key(0, 0, start_mask))

# 로컬 바인딩(미세 최적화)
stack_pop = stack.pop
stack_append = stack.append
seen_add = seen.add
seen_contains = seen.__contains__

while stack:
    x, y, mask, length = stack_pop()
    if length > ans:
        ans = length
        if ans == 26:  # 알파벳 최대치면 즉시 종료 가능
            break

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            bit = 1 << arr[nx][ny]
            if mask & bit:
                continue
            nmask = mask | bit
            key = (nmask << 10) | (nx << 5) | ny
            if not seen_contains(key):
                seen_add(key)
                stack_append((nx, ny, nmask, length + 1))

print(ans)
