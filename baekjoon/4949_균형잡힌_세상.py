import sys

def is_balanced(sentence):
    stack = []
    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()
    
    return "yes" if not stack else "no"

# 입력 처리
while True:
    line = sys.stdin.readline().rstrip()  # 개행 문자 제거
    if line == ".":  # 종료 조건
        break
    print(is_balanced(line))
