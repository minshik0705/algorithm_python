import sys
#sys.stdin = open("input.txt", 'r')

def DFS(x,y):
    if dy[x][y]>0:
        return dy[x][y]
    
    if x==0 and y==0:
        return arr[0][0]
    else:
        if y==0:
            dy[x][y]=DFS(x-1,y)+arr[x][y]
        elif x==0:
            dy[x][y]=DFS(x,y-1)+arr[x][y]
        else:
            dy[x][y]=min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]
        return dy[x][y]
            
    

if __name__=="__main__":
    n,m=map(int,input().split())
    dy=[0]*(m+1);
    for i in range(n):
        w,v=map(int,input().split())
        for j in range(w,m+1):
            dy[j]=max(dy[j], dy[j-w]+v)
    print(dy[m])
    
