'''
5.회의 배정(그리디 알고리즘)
'''
import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
meeting=[]
for i in range(n):
    s, e=map(int, input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x: (x[1], x[0]))
#key=...부분을 생략하면 원래는 s를 기준으로 정렬을 함
et=0
cnt=0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)
