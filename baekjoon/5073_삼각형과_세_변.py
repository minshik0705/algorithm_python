triangle = [1] * 3
while 1:
  triangle = list(map(int, input().split(' ',3)))
  triangle.sort()
  if triangle == [0,0,0]:
    break
  elif triangle[0] + triangle[1] <= triangle[2]:
    print('Invalid')
  elif triangle[0] == triangle[1] and triangle[1] == triangle[2]:
    print('Equilateral')
  elif triangle[0] != triangle[1] and triangle[1] != triangle[2]:
    print('Scalene')
  else:
    print('Isosceles')