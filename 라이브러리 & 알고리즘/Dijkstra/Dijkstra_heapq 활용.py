import heapq
import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')
INF = int(1e9)                  # 무한값

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
node_cost_list = [[] for i in range(n+1)]           # 노드번호가 1번부터라서 +1
# 최단거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    node_cost_list[a].append((b,c))

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))       # 0. 시작노드 q에 넣기 (비용이 0, 시작노드)       ★ 낮은 비용의 노드만 체크하는 우선순위큐 활용!
#     distance[start] = 0                 # 1. 시작노드 비용 0으로 변경
#     while q:                            # 2. q가 비어있지 않다면 반복수행
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:        # 3. 이미 처리된 노드의 비용이 현재 비용보다 낮으면 체크 필요없음
#             continue
#         for i in node_cost_list[now]:   # 4. 노드 비용 리스트에서 현재값에 대해서 방문가능한 노드 확인
#             cost = dist + i[1]          # 5. 현재노드의 비용 + 이동 비용 i[1] = cost
#             if cost < distance[i[0]]:   # 6. 다음 노드 i[0]에 해당되는 비용 distance가 cost 보다 작으면
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
#
# dijkstra(start)
# print(distance)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in node_cost_list[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[1]))

dijkstra(start)
print(distance)