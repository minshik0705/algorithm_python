import sys, re

pattern = re.compile(r'^[A-F]?A+F+C+[A-F]?$')

T = int(sys.stdin.readline())
for _ in range(T):
    s = sys.stdin.readline().strip()
    print("Infected!" if pattern.match(s) else "Good")