n, m = map(int, input().split())
y, x, d = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

# visited = [[0]*m for i in range(n)]

#    북† 동→ 남↓, 서←
# 반시계방향 다음방향 nd = (d + 3)%4
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]



answer = 0
def dfs(cy, cx, d):
    global answer
    if graph[cy][cx] == 0:
        answer +=1
        graph[cy][cx] = 2
    for i in range(4):
        # 가상으로 왼쪽 90도를 돌아서
        nd = (d + 3) % 4
        ny, nx = cy + dy[nd], cx + dx[nd] # 왼쪽 90도 앞 한칸이
        # 청소가 가능하면?
        if graph[ny][nx] == 0:
            dfs(ny, nx, nd)             # 전진 + 90도 회전해서 1번으로 돌아감
            return                      # 4방향 체크와 아래 모든 구문을 다돈 후 dfs를 완료시키기 위한 return (재귀함수의 종료조건 반드시 필요!)
        d = nd                          # 청소가 불가하면 회전방향 반영함

    # 4방향 칸 중 청소되지 않은 빈칸이 없는경우
    # 바라보는 방향을 유지한채로 한칸 후진이 가능하면?  (후진은 (d+2)%4로도 방향전환 가능)
    ny, nx = cy - dy[d], cx - dx[d]
    if graph[ny][nx] == 1:
        return
    dfs(ny, nx, d)                      # 후진 1칸 한후 1번으로 돌아감


dfs(y, x, d)
print(answer)