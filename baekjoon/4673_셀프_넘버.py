self_numbers = [0] * 10001
for idx, value in enumerate(self_numbers):
    tmp = 0
    if idx == 0:
        continue
    string = list(str(idx))
    for s in string:
        tmp += int(s)
    if idx + tmp <= 10000:
        self_numbers[idx + tmp] = 1
    if value == 0:
        print(idx)

    elif value != 0:
        continue