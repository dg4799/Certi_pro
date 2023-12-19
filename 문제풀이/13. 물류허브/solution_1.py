from collections import defaultdict
from heapq import heappush, heappop

# import sys

INC = defaultdict(list)
rINC = defaultdict(list)
INF = float('inf')


def init(N, sCity, eCity, mCost):
    global INC, rINC
    INC = defaultdict(list)
    rINC = defaultdict(list)
    for s, e, cost in zip(sCity, eCity, mCost):
        INC[s].append((e, cost))
        rINC[e].append((s, cost))
    return len(INC)


def add(sCity, eCity, mCost):
    INC[sCity].append((eCity, mCost))
    rINC[eCity].append((sCity, mCost))


def dijkstra(mHub, graph):
    distance = {city: INF for city in graph}
    distance[mHub] = 0

    q = list()  # list of tuple
    heappush(q, (0, mHub))
    while q:
        curr_cost, curr_city = heappop(q)
        if distance[curr_city] < curr_cost:
            continue
        for adj, w in graph[curr_city]:
            if w + curr_cost < distance[adj]:
                distance[adj] = w + curr_cost
                heappush(q, (w + curr_cost, adj))

    return sum(distance.values())


def cost(mHub):
    return dijkstra(mHub, INC) + dijkstra(mHub, rINC)