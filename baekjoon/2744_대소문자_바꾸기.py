import sys
string = sys.stdin.readline().strip()
for char in string:
    if char == char.upper():
        print(char.lower(), end = '')
    else:
        print(char.upper(), end = '')