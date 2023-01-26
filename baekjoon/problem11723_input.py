'''
문제11723번 
'''
M=int(input())
S=set()
'''
for i in range(M):
    '''
    #op, num=map(str, input().split())
    #num=int(num)
'''
    x=input().split()
    print(x)
    op=x[0]
    num=x[1]
    if op=='all':
        S={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif op=='empty':
        S=None
    elif op=='add':
        S.add(num)
    elif op=='remove':
        S.discard(num)
    elif op=='check':
        if num in S:
            print(1)
        else:
            print(0)
    elif op=='toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
'''
for i in range(M):
    x=input().split()

    if len(x)==1:
        op=x[0]
    else:
        op=x[0]
        num=x[1]
    if op=='all':
        S={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif op=='empty':
        S.clear()
    elif op=='add':
        S.add(num)
    elif op=='remove':
        S.discard(num)
    elif op=='check':
            print(1 if int(x[1]) in S else 0)
    elif op=='toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    
        
