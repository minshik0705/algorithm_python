import sys
A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

num = str(A * B * C)
numbers = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for n in num:
    numbers[n] += 1
for number in numbers:
    print(numbers.get(number))