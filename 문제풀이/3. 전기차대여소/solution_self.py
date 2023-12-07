import heapq
from typing import List
from collections import defaultdict

# 주유소간의 거리를 알아야함 -> BFS로 주유소간 거리 저장
# 시작위치부터 특정위치까지의 거리를 구해야함 -> 주유소간 거리를 dijkstra로 갱신
# * dijkstra도 BFS와 유사함, q에 시작노드부터 넣고 연결된 다음노드를 꺼내서 비교후 갱신되면 q에 넣어 그 다음 노드를 탐색
# - 주유소 개수 만큼 비용(INF) 배열 생성
# - 시작위치의 비용은 0으로 갱신
# - q에 시작위치를 넣고 시작
# - 주유소간 거리 리스트에서 시작위치에 연결된 다음위치와 비용을 꺼냄
# - 총 합산 비용을 계산하고 비용배열을 갱신함
# - 비용배열이 갱신되면 그 위치에 연결된 노드를 탐색하기 위해 q에 합산비용과 해당위치를 넣음
# - 모두 돌아가면 비용배열이 모두 갱신됨.

def init(N:int, mRange:int, mMap:List[List[int]]) -> None:
    global charge_range, graph, charger_list, graph_size, dist_list, charger_count
    graph_size = N
    charge_range = mRange
    graph = mMap
    charger_count = 0
    charger_list = defaultdict(list)
    dist_list = defaultdict(set)     # mID마다 서로 거리가 중복될 수 있으므로 set dict를 만듬
    return


# add로 주유소의 위치를 받으면
# 주유소의 위치를 그래프에 추가한다 (이때 벽과 구분하기위해 10을 더해줌)
# 처음 입력받은 주유소부터 BFS로 다음 주유소까지 거리를 찾는다
# 주유소를 찾으면 -10으로 본래 mID로 바꿔서 dist_list에 저장
# 이때 주유소 서로의 거리가 동일하므로 각각 저장한다
# dist_list[현재주유소].add((다음주유소, 거리))
# dist_list[다음주유소].add((현재주유소, 거리))
def add(mID:int, mRow:int, mCol:int)-> None:
    global charge_range, graph, graph_size, charge_range,dist_list, charger_count

    charger_count += 1
    # 주유소를 graph에 저장
    graph[mRow][mCol] = mID + 10
    visited = [[0] * graph_size for _ in range(graph_size)]
    y, x = (mRow, mCol)
    q = []
    visited[y][x] = 1
    dist = 0
    heapq.heappush(q, (dist, y, x))
    while q:
        dist, cy, cx = q.pop(0)
        # charge_range 보다 dist가 크면 더 이상 이동 불가로 continue
        if dist >= charge_range: continue
        for dy, dx in ((-1,0), (1,0), (0,-1), (0,1)):
            ny, nx = cy + dy, cx + dx
            if not 0 <= nx < graph_size: continue
            if not 0 <= ny < graph_size: continue
            if graph[ny][nx] == 1 and visited[ny][nx] == 1: continue
            if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                # q에 이동 거리와 좌표를 push
                heapq.heappush(q, (dist+1, ny, nx))
            if graph[ny][nx] >= 10 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                next_mID = graph[ny][nx] - 10
                # dist_list에 주유소간의 거리를 저장함 {주유소 : (다음주유소, 거리)}
                dist_list[mID].add((next_mID, dist+1))
                dist_list[next_mID].add((mID, dist+1))
                continue
    return



# Dijkstra로 각 주유소까지의 거리배열을 갱신
def distance(mFrom:int, mTo:int)-> int:
    global charge_range, graph, dist_list, graph_size, charger_count
    start = mFrom

    # 주유소까지의 거리배열 cost_list
    cost_list = [int(1e9)] * (charger_count + 1)

    q = []
    # 시작 위치는 거리가 없으므로 0
    cost_list[start] = 0
    # q에 (거리, 시작위치)를 넣음, 앞의 숫자로 낮은것부터 빠르게
    heapq.heappush(q, (0, start))
    while q:
        # 거리, 현재위치를 뽑음
        dist, now = heapq.heappop(q)
        # cost_list의 현재위치의 값이 거리보다 낮으면 continue (비용이 더 크므로 갱신 X)
        if cost_list[now] < dist:
            continue
        # for문으로 dist_list에서 현재위치에 연결된 다음 위치를 꺼냄
        for i in dist_list[now]:
            # 비용 = 현재 위치의 비용 + 다음 위치의 까지의 비용
            cost = dist + i[1]
            # 비용이 cost_list의 현재위치의 비용이 cost보다 크면 (해당 위치에 도달하기위한 비용 = cost)
            if cost < cost_list[i[0]]:
                # cost_list의 현재 비용을 cost로 갱신
                cost_list[i[0]] = cost
                # q에 합산 비용 cost와 연결된 위치 i[[0]를 넣어 다시 해당 위치에서 연결된 위치로 돌림
                heapq.heappush(q, (cost, i[0]))
    if cost_list[mTo] == int(1e9):
        return -1
    return cost_list[mTo]


