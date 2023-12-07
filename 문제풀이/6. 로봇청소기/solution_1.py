n, m=map(int, input().split())
cur=list(map(int, input().split()))
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer=0
def dfs(y, x, d):
    global answer
    if graph[y][x]==0:
        answer+=1
        graph[y][x]=2
    for _ in range(4):
        nd=(d+3)%4
        ny=y+dy[nd]
        nx=x+dx[nd]
        if graph[ny][nx]==0:
            dfs(ny, nx, nd)
            return
        d=nd
    nd=(d+2)%4
    ny=y+dy[nd]
    nx=x+dx[nd]
    if graph[ny][nx]==1:
        return
    dfs(ny, nx, d)
dfs(cur[0], cur[1], cur[2])
print(answer)