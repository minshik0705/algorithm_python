import sys

# 입력
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# 행/열/박스 사용숫자 비트마스크 (1~9 -> 비트 0~8)
row = [0]*9
col = [0]*9
box = [0]*a9
empties = []

def bidx(r, c):
    return (r//3)*3 + (c//3)

# 초기 마스크 설정 및 빈칸 수집
for r in range(9):
    for c in range(9):
        v = board[r][c]
        if v == 0:
            empties.append((r, c))
        else:
            bit = 1 << (v-1)
            row[r] |= bit
            col[c] |= bit
            box[bidx(r, c)] |= bit

ALL = (1 << 9) - 1  # 0b1_1111_1111

def candidates_mask(r, c):
    used = row[r] | col[c] | box[bidx(r, c)]
    return ALL ^ used  # 사용되지 않은 비트가 후보

def pick_next():  # MRV: 후보가 가장 적은 칸 고르기
    best_i = -1
    best_count = 10
    best_mask = 0
    for i, (r, c) in enumerate(empties):
        if board[r][c] != 0:
            continue
        m = candidates_mask(r, c)
        cnt = m.bit_count()
        if cnt < best_count:
            best_count = cnt
            best_mask = m
            best_i = i
            if cnt == 1:
                break
    return best_i, best_mask

def solve(left):
    if left == 0:
        return True

    idx, cmask = pick_next()
    if idx == -1:
        return False  # 방어적
    r, c = empties[idx]

    # 후보 숫자 순회 (비트 하나씩 꺼내기)
    m = cmask
    while m:
        bit = m & -m
        m -= bit
        v = (bit.bit_length() - 1) + 1  # 1..9
        b = bidx(r, c)
        # 배치
        board[r][c] = v
        row[r] |= bit
        col[c] |= bit
        box[b] |= bit

        if solve(left - 1):
            return True

        # 되돌리기
        board[r][c] = 0
        row[r] ^= bit
        col[c] ^= bit
        box[b] ^= bit

    return False

solve(len(empties))

# 출력
out = []
for r in range(9):
    out.append(" ".join(map(str, board[r])))
print("\n".join(out))
