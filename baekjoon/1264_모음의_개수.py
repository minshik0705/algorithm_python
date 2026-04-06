import sys, re
 
input = sys.stdin.readline
 
vowels = ['a', 'e', 'i', 'o', 'u']

string = ''

while True:
    count = 0
    string = input().strip()
    if string == '#':
        break
    for char in string:
        char = char.lower()
        if char in vowels:
            count += 1
    print(count)