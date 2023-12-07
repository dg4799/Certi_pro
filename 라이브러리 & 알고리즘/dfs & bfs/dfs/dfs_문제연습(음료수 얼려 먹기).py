"""
N * M 크기의 얼음 틀
0 : 구멍이 뚫려있는 부분
1 : 칸막이

0이 붙어있으면 하나의 아이스크림
0이 붙어있는 덩어리의 개수

- 특정지점의 주변 상, 하, 좌, 우를 살펴봄
- 0이면서 방문하지 않은 지점이 있으면 해당지점 방문
- 연결된 모든 지점을 방문
-
"""
import sys
sys.stdin = open("sample_input.txt", "r")

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]


# 동서남북 방향
dy = [0, 0, -1, 1]
dx = [1,-1, 0, 0]
def dfs(sy, sx):
    if sx < 0 or sy < 0 or sx > m-1 or sy > n-1:
        return False    # 방문 불가한 지점, return으로 빠져나옴
    if graph[sy][sx] == 0: # 방문가능하다면
        graph[sy][sx] = 2  # 방문처리
        for i in range(4):
            ny, nx = sy+dy[i], sx+dx[i]
            for i in range(n):
                print(graph[i])
            print()
            dfs(ny, nx)

        return True     # 방문가능한 위치에 들어가서 다돌아서 나오며 방문처리함, 방문가능한 지점이 있었으므로 True 반환
    return False        # 방문가능한 지점이 없었으므로 False


# 모든 노드(위치에) 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:  # 방문가능한 점이 있으면, dfs로 들어가서
                               # 동 -> 동1 -> 방문불가(Return) -> 동1(Return) -> 동(Return) -> 서 -> 서1 -> 방문불가(Return) ..
                               # 연결된 모든 곳은 dfs로 방문처리됨
            result += 1
print(result)
