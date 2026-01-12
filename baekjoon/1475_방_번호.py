import sys
numbers = '0123456789'
num_dict = dict()
for num in numbers:
    num_dict[num] = 0
room = sys.stdin.readline().strip()

for n in room:
    if n == '6' and num_dict['6'] > num_dict['9']:
        num_dict['9'] += 1
    elif n == '9' and num_dict['9'] > num_dict['6']:
        num_dict['6'] += 1
    else:
        num_dict[n] += 1
print(max(num_dict.values()))