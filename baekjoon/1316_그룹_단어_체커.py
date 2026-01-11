import sys
N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]

def dedup_keep_order(s: str) -> str:
    # 키 등장 순서를 유지하면서 중복 제거
    return ''.join(dict.fromkeys(s))

check = [dedup_keep_order(w) for w in words]

answer = 0
for word, ch in zip(words, check):
    w = list(word)
    c = list(ch)
    while c and w:
        if w[0] == c[0]:
            w.pop(0)
        else:
            c.pop(0)
    if not w:
        answer += 1
print(answer)