K, N = map(int, input().split())
lanline = []
for _ in range(K):
  lanline.append(int(input()))

start = 1
end = max(lanline)
mid = (start+end) // 2
count = sum(num // mid for num in lanline)

while start <= end:
  mid = (start+end) // 2
  count = sum(num // mid for num in lanline)
  if count >= N:
    start = mid + 1
  elif count < N:
    end = mid - 1
print(end)