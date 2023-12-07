"""
스택구조를 활용해서 시작노드에서 방문가능한 노드로 들어가고 방문처리
다시 그 노드에서 방문가능한 노드로 들어가서 방문처리
방문하지 못할때까지 연결된 노드를 들어갔다가 방문하기 못하게되면
재귀를 복귀하면서 방문가능한 노드가 있는 노드까지 돌아감.
다시 그 노드부터 방문가능한 노드를 찾아 들어가서 방문처리..
한방향으로 막힐때까지 반복 탐색하는 완전탐색 얼고리즘
"""

# 1차원 리스트 graph
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# visited 생성
visited = [False] * 9 # 0번 노드는 사용안해서 +1

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True   # 들어간 노드의 방문처리(시작~재귀로 들어가서)
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:  # 1번 노드가 방문가능한 2, 3, 8 중 2부터 들어감
        if not visited[i]: # 2번 노드가 방문되지 않았으면 방문(방문처리는 함수 들어가서 처음에함)
            dfs(graph, i, visited) # 계속해서 방문 가능한 노드로 들어가서
                                   # 방문이 불가하면 함수를 종료하면서 되돌아나옴

dfs(graph, 1, visited)
