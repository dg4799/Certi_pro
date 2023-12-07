global visit, d, dx, dy, rev
d = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
rev = [2, 3, 0, 1]


def dfs(x: int, y: int, scanFromRobot, moveRobot) -> None:
    global visit, d, dx, dy, rev
    W = 0  ## tmp 방향
    st = [[0] * 3 for _ in range(3)]  ## 받아올 배열
    scanFromRobot(st)  ## st 업데이트

    for i in range(4):  ## 4방향 길 있는지 검사
        nd = (d + W) % 4  ## 현재방향 + tmp 방향 = 다음방향
        nx = x + dx[nd]
        ny = y + dy[nd]
        if st[1 + dx[i]][1 + dy[i]] or visit[nx][ny]:  ## 갈수 있는 곳인지 검사
            W += 1  ## 갈수없거나 이미 방문한 곳이면 다른 방향으로
            continue

        moveRobot(W % 4)  ## 1칸 이동
        visit[nx][ny] = 1  ## 방문한 지역 표시
        d = nd  ## 현재 방향 업데이트

        dfs(nx, ny, scanFromRobot, moveRobot)  ## 위 행위 반복

        moveRobot((rev[nd] - d + 4) % 4)  ## 현 위치에서 모두 방문했을때 위치 재설정?
        d = rev[nd]  ## 방향 재설정 ??
        W = 3  ## ??


def init(N: int, subTaskCount: int):
    return


def cleanHouse(mLimitMoveCount: int, scanFromRobot, moveRobot):
    global visit
    visit = [[0] * 30 for _ in range(30)]
    dfs(0, 0, scanFromRobot, moveRobot)