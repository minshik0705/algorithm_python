import sys
string = list(sys.stdin.readline().strip())
string.sort(reverse = True)
print(''.join(string))