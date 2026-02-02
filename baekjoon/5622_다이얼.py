inputed = input().strip()
 
dial = {
    "ABC" : 3,
    "DEF" : 4,
    "GHI" : 5,
    "JKL" : 6,
    "MNO" : 7,
    "PQRS" : 8,
    "TUV" : 9,
    "WXYZ" : 10,
}
result = 0

for string in inputed:
    for d in dial:
        if string in d:
            result += dial[d]
print(result)