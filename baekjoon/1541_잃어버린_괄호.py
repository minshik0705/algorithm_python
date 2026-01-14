import sys

expr = sys.stdin.readline().strip()
parts = expr.split('-')

def sum_part(p):
    return sum(map(int, p.split('+')))

answer = sum_part(parts[0]) - sum(sum_part(p) for p in parts[1:])
print(answer)
