inputed = input().strip()
count = 0
if not inputed:
    print(0)
else:
    for string in inputed:
        if string == ' ':
            count += 1
    print(count + 1)