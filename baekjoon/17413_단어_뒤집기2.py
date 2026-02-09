import sys
from collections import deque

sentence = sys.stdin.readline().rstrip('\n')
flag = 0
answer = []
tmp = deque()

for ch in sentence:
    if ch == '<':
        # 태그 시작 전, 쌓인 단어 먼저 flush
        while tmp:
            answer.append(tmp.popleft())
        flag = 1
        answer.append(ch)  # '<' 출력

    elif ch == '>':
        flag = 0
        answer.append(ch)  # '>' 출력

    elif flag == 1:
        # 태그 내부: 그대로
        answer.append(ch)

    else:
        # 태그 외부
        if ch == ' ':
            # 단어 끝: tmp flush 후 공백 추가
            while tmp:
                answer.append(tmp.popleft())
            answer.append(' ')
        else:
            tmp.appendleft(ch)

# 문장 끝났는데 tmp 남아있으면 flush
while tmp:
    answer.append(tmp.popleft())

print(''.join(answer))
