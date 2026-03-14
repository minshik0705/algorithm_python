import sys
N = int(sys.stdin.readline().strip())
direc = []
C = []
for i in range(N):
    A = list(sys.stdin.readline().strip())
    if i == 0:
        tmp = A
        continue
    else:
        C = tmp
        for i in range(len(A)):
            if A[i] != C[i]:
                A[i] = '?'
        tmp = A
        
print(''.join(A))