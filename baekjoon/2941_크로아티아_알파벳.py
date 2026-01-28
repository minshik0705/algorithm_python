import sys
Croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
string = str(sys.stdin.readline().strip())
alphabets = len(string)

for cro in Croatia:
    if cro in string:
        string = string.replace(cro, '*')

print(len(string))