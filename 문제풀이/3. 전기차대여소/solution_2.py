from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def init(N: int, mRange: int, mMap: List[List[int]]) -> None:
    global n, m, grid, stationCnt, distDict
    n = N
    m = mRange
    grid = mMap[:n][:n]  ## 전체 grid 저장
    stationCnt = 0
    distDict = defaultdict(lambda: defaultdict(int))  ## station간 거리 저장 위한 dict
    return


def bfs(st, ed):
    global distDict
    cID = grid[st][ed] - 1000  ##현재 station ID get ( 상수 빼주기 )
    Q = deque([(st, ed)])
    visited = [[-1] * n for _ in range(n)]  ## visited에 distance가 업데이트 될 예정이라 -1로 초기화
    visited[st][ed] = 0
    while Q:
        x, y = Q.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < n and 0 <= ny < n): continue
            if visited[nx][ny] != -1: continue
            if grid[nx][ny] == 1: continue  ## 벽이면 방문X
            nDist = visited[x][y] + 1
            if nDist > m: continue
            if grid[nx][ny] > 1:  ## station인 경우 distDict 업데이트
                print(nDist, ny, nx)
                tID = grid[nx][ny] - 1000
                distDict[cID][tID] = nDist
                distDict[tID][cID] = nDist
            Q.append((nx, ny))
            visited[nx][ny] = nDist
    pass


def add(mID: int, mRow: int, mCol: int) -> None:
    global stationCnt
    stationCnt += 1
    grid[mRow][mCol] = mID + 1000  ## grid에서 벽(1)과 혼동하지 않기위한 상수 더하기
    if stationCnt > 1:
        bfs(mRow, mCol)  ## station add 될때마다 distDict를 업데이트 해줘야함
    return


def dijkstra(x, y):
    PQ = []
    visited = [float('inf')] * stationCnt
    heappush(PQ, (x, 0))
    visited[x] = 0
    while PQ:
        cID, cDist = heappop(PQ)
        if visited[cID] < cDist:
            continue
        for nID, tDist in distDict[cID].items():
            nDist = cDist + tDist
            if nDist < visited[nID]:
                visited[nID] = nDist
                heappush(PQ, (nID, nDist))
    result = visited[y] if visited[y] != float('inf') else -1
    return result


def distance(mFrom: int, mTo: int) -> int:
    result = dijkstra(mFrom, mTo)
    return result