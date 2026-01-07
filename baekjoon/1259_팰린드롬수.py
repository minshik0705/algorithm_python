import sys
num = 1
while True:
    answer = 'yes'
    num = list(sys.stdin.readline().strip())
    length = len(num)
    if num == ['0']:
        break
    for i in range(length // 2):
        if num[i] != num[length - i - 1]:
            answer = 'no'
            break
    print(answer)