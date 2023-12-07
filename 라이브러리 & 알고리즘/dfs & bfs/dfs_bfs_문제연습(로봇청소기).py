"""
로봇청소기 문제
1. 0북,1동,2남,3서 direction이 있음
2. DFS로 이동가능한 위치까지 이동
3. 왼쪽 방향에 청소할 공간이 있으면 그 방향으로 회전 후 전진
4. 왼쪽 방향에 청소할 공간이 없다면 그 방향 회전후 3.을 체크
5. 네방향 모두 청소되었거나  이미 벽인 경우 바라보는 방향을 유지한채 한칸 후진하고 3.을 체크
6. 네방향 모두 청소되었거나 벽이면서 뒤쪽 방향이 벽이라 후진할 수 없는 경우 동작 멈춤
- 로봇은 이미 청소한 칸을 또 청소하지 않고, 벽 통과 불가능

- 네 방향을 탐색하는 함수를 만듬 (direction)
  1. ★ ★ (북(-1,0), 동(0,1), 남(1,0), 서(0,-1))
  2. cy, cx에 dx, dy를 더하면 방향회전
- 왼쪽 방향을 체크하는 함수를 만듬 (left_direction)
  (북, 동, 서, 남을 기준으로 왼쪽으로 변하는것을 체크)
  1. 북 -> 서 -> 남 -> 동  (현재가 서라면 왼쪽은 남)
     ★ ★  0  -> 3 -> 2 -> 1
  2. 왼쪽 화전을 수식화 하면 :  ★ ★ (현재방향+3)%4
    - 현재값에+3을해서 4로 나눈 나머지로 다음 값을 만들 수 있음.
"""

import sys
sys.stdin = open("input.txt", "r")

# dr : 북0, 동1, 남2, 서3
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solve(cy, cx, dr):
    cnt = 0             # 청소한 공간 수
    while True:         # 청소기가 더이상 움직이지 못할때 종료
        # [1] 현재 위치 청소
        arr[sy][cx] = 2 # 2로 청소처리
        cnt += 1

        # [2] 왼쪽방향으로 순서대로 탐색해서 미청소 영역이 있으면 이동
        #     없으면 후진
        flag = True
        while flag == True:
            # 왼쪽으로 네방향을 체크하기 위해 next_dr = (dr+3)%4
            for i in range(4):
                next_dr = (dr + 3) % 4
                dr -= 1
                ny, nx = sy+dy[next_dr], sx+dx[next_dr]
                if arr[ny][nx] == 0:    # 미청소 영역
                    cy, cx, dr = ny, nx, next_dr
                    flag = 0    # while 탈출
                    break
            else:           # 4방향 모두 미청소 영역 없음 (후진)
                by, bx = sy-dy[dr], cx-dx[dr]               # 현재 방향에 해당되는 dy, dx를 빼주면 후진
                if arr[by][bx] == 1:
                    return cnt
                else:
                    sy, sx = by, bx



N, M = map(int, input().split())
sy, sx, dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

ans = solve(sy, sx, dr)
print(ans)
