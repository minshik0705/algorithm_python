attendence = [i for i in range(30)]

for _ in range(28):
  student = int(input())
  attendence.remove(student-1)

for x in attendence:
  print(x+1)