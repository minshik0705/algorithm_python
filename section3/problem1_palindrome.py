'''
회문 검사 문제
'''

import sys
#sys.stdin=open("input.txt",'r')
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
#내풀이
'''
import sys
#sys.stdin=open("input.txt",'r')
n=int(input())
for i in range(n):
    word=input()
    word=word.upper()   #모두 대문자나 소문자로 변환하면 해결됨
    size=len(word)
    for j in range(size//2):
        if word[j]!=word[size-j-1]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
'''            
