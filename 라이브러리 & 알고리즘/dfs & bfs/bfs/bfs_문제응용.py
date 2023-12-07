import sys
sys.stdin = open("sample_input.txt", "r")


def bfs(si, sj, ei, ej):        # si, sj = 시작좌표, ei, ej = 끝좌표
    q = []
    v = [[0] * M for _ in range(N)]
    q.append((si,sj))
    v[si][sj] = 1
    while q:
        ci, cj = q.pop(0)        # 현재좌표 ci, cj
        # 정답처리 또는 종료는 이 자리에서..

        if (ci, cj) == (ei, ej):
            return v[ei][ej]


        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):  # 델타좌표(변하는값) di, dj
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = bfs(0, 0, N-1, M-1)

print(ans)
