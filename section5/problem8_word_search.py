'''
import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
p=dict()#list와 다르게 문자, 단어를 키값, 인덱스 값으로 사용가능하다
for i in range(n):
    word=input()
    p[word]=1
for i in range(n-1):
    word=input()
    p[word]=0
for key, val in p.items():
    if val==1:
        print(key)
        break
'''

def missing_word(n, word1, word2):
    return list(set(word1)-set(word2))

n=int(input())
word1=list(map(str,input().split(' ', n-1)))
word2=list(map(str,input().split(' ', n-2)))

print(word1)
print(word2)

print(missing_word(n,word1,word2))


    
