import heapq


def dijkstra(graph, start):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대(inf)로 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # 모든 정점을 저장할 큐를 생성
    queue = [(0, start)]

    while queue:
        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트
        current_distance, current_node = heapq.heappop(queue)

        # 이미 처리된 노드는 무시
        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
            # 거리를 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances


def init(N, sCity, eCity, mCost):
    global graph
    global r_graph
    graph = {}
    r_graph = {}

    for i in range(N):
        if not sCity[i] in graph:
            graph[sCity[i]] = {eCity[i]: mCost[i]}
        else:
            graph[sCity[i]].update({eCity[i]: mCost[i]})
        # reversed
        if not eCity[i] in r_graph:
            r_graph[eCity[i]] = {sCity[i]: mCost[i]}
        else:
            r_graph[eCity[i]].update({sCity[i]: mCost[i]})
    return len(graph.keys())


def add(sCity, eCity, mCost):
    global graph
    graph[sCity].update({eCity: mCost})
    r_graph[eCity].update({sCity: mCost})


def cost(mHub):
    global graph
    total_cost = 0
    forward_cost = dijkstra(graph, mHub)
    for value in forward_cost.values():
        total_cost += value
    bacward_cost = dijkstra(r_graph, mHub)
    for value in bacward_cost.values():
        total_cost += value
    # for key in graph.keys():
    #   total_cost += dijkstra(graph, key)[mHub]

    return total_cost

# init(10, [3,1,5,5,3,5,1,4,2,4], [2,4,3,4,5,2,5,1,3,5], [46,15,30,31,23,47,35,24,32,13])
# print(cost(5))
# add(5, 1, 24)
# print(cost(5))
# add(2, 1, 11)
# print(cost(4))