import sys
'''
#sys.stdin=open("input.txt", "r")
a=input()
b=input()
str1=dict()
str2=dict()
for x in a:
    str1[x]=str1.get(x,0)+1#str1의 value값을 +1해라
for x in b:
    str2[x]=str2.get(x,0)+1

for i in str1.keys():#각 문자를 확인하면
    if i in str2.keys():#str2에도 같은 키값을 가진다면
        if str1[i]!=str2[i]:#다른 값을 가진다면
            print("NO")
            break
    else:#애초에 문자가 존재하지 않는다면
        print("NO")
        break
else:
    print("YES")
'''   


a=input()
b=input()
chara1=list(a)
chara2=list(b)
chara1.sort()
chara2.sort()

if chara1==chara2:
    print('YES')
else:
    print('NO')


