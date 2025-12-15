import sys

input = sys.stdin.readline
write = sys.stdout.write

M = int(input())
S = 0                      # 1~20을 비트로 표현 (1이면 포함)
ALL = (1 << 20) - 1        # 20비트가 전부 1인 값

for _ in range(M):
    parts = input().split()
    cmd = parts[0]

    if cmd == 'all':
        S = ALL
    elif cmd == 'empty':
        S = 0
    else:
        x = int(parts[1]) - 1  # 0~19로 맞추기
        bit = 1 << x
        if cmd == 'add':
            S |= bit
        elif cmd == 'remove':
            S &= ~bit
        elif cmd == 'check':
            # 출력 즉시 write (버퍼에 쌓지 않음)
            write('1\n' if (S & bit) else '0\n')
        elif cmd == 'toggle':
            S ^= bit
