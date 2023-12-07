import sys
sys.stdin = open("sample_input.txt", "r")

N, M = map(int, input().split())
print(N, M)
arr = [list(map(int, input())) for _ in range(N)]

def bfs(sx, sy, ex, ey):
    q = [(sx, sy)]
    visited = [[0] * M for _ in range(N)]
    visited[sx][sy] = 1
    while q:
        cx, cy = q.pop()    # 현재위치 ci, cj

        if (cx, cy) == (ex, ey):
            return visited[cx][cy]

        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            nx, ny = cx+dx, cy+dy   # dx, dy(방향)을 더한 cx, cy를 다음위치인 nx, ny에 저장
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                visited[nx][ny] = visited[cx][cy]+1
                q.append((nx, ny))

                for i in range(N):
                    print(visited[i])
                print()

print(bfs(0,0,N-1, M-1))


# 출발 좌표 sx, sy와 종료 좌표 ex, ey를 입력값으로 받는다
# visited를 [0]으로 같은 갯수로 배열을 만든다
# q를 만들고 sx와 sy를 넣고 visited의 sx, sy에도 1로 방문처리 한다.
# while을 q로 돌린다. (q가 있을때까지 돌아감)
# q에서 값을 꺼내는데 현재위치 cx, cy를 꺼낸다
# 그리고 방향을 더해주는 dx, dy를 4방향 for문을 돌린다
# cx, cy에 dx, dy를 더해 다음 체크할 위치 nx, ny를 만든다
# nx, ny가 범위를 벗어나지 않는지 and arr의 이동가능한 위치 and visited에 방문한적이 없는지 if로 체크해서
# 해당되면 visited에 방문처리를 하는데 도착지점의 거리수를 알아야하기 때문에 방문처리를 현재값+1씩 처리한다
# 그리고 해당 위치를 q에 넣는다.
# 도착위치에 해당되면 bfs를 종료해야하므로 현재위치를 꺼낸 다음자리에 조건을 체크해서 값을 return하고 종료


# 값을 받고 visited를 만들고 q에 시작위치를 넣으면서 visited 시작위치를 방문처리
# while을 q로 돌리고 q에서 값을 뽑고 체크해야할 조건(방향 등) dx dy를 만들고 q로 뽑은 값에 더해주면
# 다음 체크할 값이 됨
# 체크할 값으로 범위를 벗어나는지 확인 및 체크해야할 조건(이동가능 등)을 만족하면
# 해당위치 visited를 방문처리하고 q에 넣어 다음 bfs를 돌게끔함.
# visited의 방문처리를 할때 카운트를 하면됌!!!!