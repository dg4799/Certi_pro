global visit, d, dx, dy, rev
d = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
rev = [2, 3, 0, 1]


def dfs(x: int, y: int, scanFromRobot, moveRobot) -> None:
    global visit, d, dx, dy, rev

    # 임시 방향 0
    W = 0  ## tmp 방향
    # 받아올 3*3 배열
    st = [[0] * 3 for _ in range(3)]  ## 받아올 배열
    # 배열 받아옴
    scanFromRobot(st)  ## st 업데이트

    # 서, 북, 동, 남으로 4방향 체크
    for i in range(4):  ## 4방향 길 있는지 검사
        # (현재방향 + 임시방향) % 4 => 나머지가 다음방향 +1(3이면 0으로 바뀜)
        nd = (d + W) % 4  ## 현재방향 + tmp 방향 = 다음방향
        # x, y에 dx[0~3]을 더해서 4방향의 nx, ny를 만듬
        nx = x + dx[nd]
        ny = y + dy[nd]
        # st의 가운데인 1,1에 dx(0~3)을 더해서 방문 가능한 곳인지 찾음
        # 동시에 visit에 nx, ny로 갈 수 있는 곳인지 검사(이직 방향 모름)
        if st[1 + dx[i]][1 + dy[i]] or visit[nx][ny]:  ## 갈수 있는 곳인지 검사
            # 갈수 없으면 임시방향 1을 올려 방향을 돌림
            W += 1  ## 갈수없거나 이미 방문한 곳이면 다른 방향으로
            continue

        # 갈수 있는 곳이면
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