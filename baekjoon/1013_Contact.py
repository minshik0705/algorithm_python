import sys, re
 
input = sys.stdin.readline
 
T = int(input().strip())

pattern = re.compile(r'((100+1+)|(01))+')

for _ in range(T):
    string = input().strip()
    if pattern.fullmatch(string):
        print('YES')
    else:
        print('NO')