import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start = 1
end = max(trees)

while start <= end:
  mid = (start + end) // 2
  tot = 0 #벌목한 나무의 총 길이
  #벌목한 나무의 총 길이 구하기
  for log in trees:
    if log >= mid:
      tot += log - mid
  #이분탐색 알고리즘
  if tot >= M:#만약 나무 총 길이가 너무 크다면
    start = mid + 1 #자르는 길이를 늘린다
  else:#만약 나무 총 길이가 작다면
    end = mid -1 #자르는 길이를 줄인다
print(end)#가장 마지막으로 자른길이가 최대길이가 된다