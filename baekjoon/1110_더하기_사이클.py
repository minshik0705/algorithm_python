#N= list(map(int,input().strip()))-> 해당 코드의 경우 한자리수는 처리를 못한다
num = int(input())
N = [num//10, num%10]
origin = list(N) #origin = N을 사용하면 메모리내에 같은 공간을 사용하게 된다
count = 0
while 1:
  tot = sum(N) % 10
  temp = N[1]
  N[1] = tot
  N[0] = temp
  count += 1
  if N == origin:
    break
print(count)