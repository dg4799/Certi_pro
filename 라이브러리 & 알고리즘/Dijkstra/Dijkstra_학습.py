"""
https://www.youtube.com/watch?v=F-tkqjUiik0

가장 짧은 경로를 찾는 알고리즘
 - 한 지점에서 다른 한지점 까지의 최단 경로
 - 한 지점에서 다른 모든 지점까지의 최단 경로
 - 모든 지점에서 모든지점 까지의 최단 경로


각 노드들 간의 비용(거리)를 가지고 목적지 노드까지 비용(거리)를 비교하고 적은 비용으로 갱신하며 최단 경로 찾음

★ 각 노드들간의 비용이 dict로 저장되어 있어야 함
 - {0번 : (1번까지, 비용 5), 1번 : (0번까지, 비용 5) ...}
 - dict를 만들고 key(시작노드), value(다음노드, 비용)으로 dict 만들것!


1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화
 - 모든 노드까지의 비용을 '무한'으로 설정
 - 자기 자신에 대한 노드는 0으로 설정
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3~4번을 반복

1,   2,   3,   4,   5,   6
0, inf, inf, inf, inf, inf
- 1번부터 연결된 노드중(방문 가능한 노드) 가장 작은 비용의 노드부터 방문
- 1이 0이므로 (0+노드까지 거리)가 현재 값보다 작으면 갱신

1,   2,   3,   4,   5,   6
0,   2,   5,   1, inf, inf
- 그리고 갱신된 배열에서 가장 적은 비용의 노드인 4번 부터 방문 가능한 노드들의 비용을 계싼
- 1 -> 4의 비용이 1이므로 (1+노드까지 거리)가 현재값보다 작으면 갱신

"""
import sys
input = sys.stdin.readline()
INF = int(1e9)   # 10억을 무한의 값으로 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 방문한적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번으로 가는 비용이 c라는 의미
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서 가장 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF                                     # INF부터 시작
    index = 0                                           # 가장 최단 거리의 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:  # distance[i]부터 방문하지 않은 i가 min_value보다 낮으면
            min_value = distance[i]                     # min_value에 거리값을 넣고
            index = i                                   # index를 업데이트함
    return index                                        # 모두 돌아보면 가장 적은 value의 indexl 나옴

# 다익스트라 알고리즘
def dijkstra(start):
    distance[start] = 0                                 # 출발노드
    visited[start] = True                               # 출발노드 방문처리

    for j in graph[start]:                              # 출발노드가 방문가능한 노드를 꺼내서 비용을 넣음
        distance[j[0]] = j[1]                           # 방문 가능한 노드(j[0]), 비용(j[1])

    for i in range(n-1):                                # 그리고 각 노드별로 체크
        now = get_smallest_node()                       # 현재 가장 최단거리인 노드를 꺼내서
        visited[now] = True                             # 방문처리하고
        for j in graph[now]:                            # 현재 노드와 연결된 다른 노드 확인
            cost = distance[now] + j[1]                 # 현재노드의 비용 + 연결된 다른노드 까지 비용
            if cost < distance[j[0]]:                   # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더짧으면
                distance[j[0]] = cost                   # 최단거리 값을 갱신함

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:      # 도달할 수 없는 경우, 무한으로 출력
        print("INF")
    else:                       # 도달할 수 있는 경우
        print(distance[i])