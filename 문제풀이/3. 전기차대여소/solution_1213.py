"""

-add
  1. mRow, mCol에 대여소가 설치됨
  2. 대여소가 설치되면 bfs로 대여소간 mRange 이하로 방문 가능한 위치를 저장
  3. charger[]를 만들고 대여소와 대여소간의 거리를 저장해둠

-distance
  1. mFrom, mTo를 받아 최단거리를 return
  2. 다익스트라로 mFrom 부터 시작하는 최단경로를 만든다.
   - INF배열을 만든다
   - q를 만들고 q에 넣고 while 시작 (시작지점 거리는 0)
   - pop을 해서 현재 dist, mID를 뽑음
   - charger[]에 now를 넣어 next_mid와 dist를 뽑는다
   - 현재 dist + next_mid dist로 cost를 구하고 INF배열의 cost[now]와 비교한다
   - INF배열의 cost[now]보다 낮으면 cost[now]를 갱신
   - q에 cost, next_mid를 넣어 다시 돌림

"""

from typing import List
from collections import defaultdict, deque


def init(N: int, mRange: int, mMap: List[List[int]]) -> None:
    global Size, charge_count, graph, charger, dx, dy
    Size = N
    charge_count = mRange
    graph = mMap
    charger = defaultdict(list)

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    return


def add(mID: int, mRow: int, mCol: int) -> None:
    """
    -add
  1. mRow, mCol에 대여소가 설치됨
  2. 대여소가 설치되면 bfs로 대여소간 mRange 이하로 방문 가능한 위치를 저장
  3. charger[]를 만들고 대여소와 대여소간의 거리를 저장해둠
    """
    global charge_count, graph, charger, dx, dy, Size, last_mID
    last_mID = mID
    graph[mRow][mCol] = mID + 10
    visted = [[False for i in range(Size)] for i in range(Size)]

    # bfs
    Queue = deque()
    Queue.append((mRow, mCol, charge_count))
    visted[mRow][mCol] = True

    while Queue:
        cy, cx, c_count = Queue.popleft()
        if c_count == 0: continue
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < Size and 0 <= nx < Size and graph[ny][nx] != 1 and visted[ny][nx] == False:
                if graph[ny][nx] >= 10:
                    charger[graph[ny][nx] - 10].append((graph[mRow][mCol] - 10, charge_count - (c_count - 1)))
                    charger[graph[mRow][mCol] - 10].append((graph[ny][nx] - 10, charge_count - (c_count - 1)))
                    visted[ny][nx] = True
                else:
                    visted[ny][nx] = True
                    Queue.append((ny, nx, c_count - 1))

    return


def distance(mFrom: int, mTo: int) -> int:
    """
    -distance
  1. mFrom, mTo를 받아 최단거리를 return
  2. 다익스트라로 mFrom 부터 시작하는 최단경로를 만든다.
   - INF배열을 만든다
   - q를 만들고 q에 넣고 while 시작 (시작지점 거리는 0)
   - pop을 해서 현재 dist, mID를 뽑음
   - charger[]에 now를 넣어 next_mid와 dist를 뽑는다
   - 현재 dist + next_mid dist로 cost를 구하고 INF배열의 cost[now]와 비교한다
   - INF배열의 cost[now]보다 낮으면 cost[now]를 갱신
   - q에 cost, next_mid를 넣어 다시 돌림
    """
    global charge_count, graph, charger, dx, dy, Size, last_mID

    # 다익스트라
    INF_list = [10000 for i in range(200)]
    Queue = deque()
    Queue.append((0, mFrom))
    INF_list[mFrom] = 0
    while Queue:
        dist, now = Queue.popleft()
        for i in charger[now]:
            next_mid, next_dist = i[0], i[1]
            cost = dist + next_dist
            if cost < INF_list[next_mid]:
                INF_list[next_mid] = cost
                Queue.append((cost, next_mid))

    if INF_list[mTo] == 10000:
        return -1

    return INF_list[mTo]


"""
(★오답) 일부 케이스만 실패하는 경우 리스트에 저장되는 거리 or 비용에서 잘못 합산이 되는게 아닌지 살펴볼 것!
        ex) charger에 거리값을 append 할때 c_count가 다른 로직에서 -= 1이 반영되어 값이 이상하게 들어가는 경우가 있었음
        -=1/+=1은 값이 지속적으로 감소/증가 하는 경우만 사용하고 아닌 경우 값에 바로 -1 or +1을 바로 넣을것.
"""