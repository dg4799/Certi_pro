def init(N):
    global parents, scores, n
    n = N + 1  # 0은 버리고 1~n
    parents = [i for i in range(n)]  # parent node
    scores = [0 for _ in range(n)]  # 부모노드와의 점수차
    pass


def updateScore(mWinnerID, mLoserID, mScore):
    # 각 노드의 최상위 부모 노드를 찾는다. (최상위 부모 노드에만 값을 반영하면 됌)
    winner_root, loser_root = find_root(mWinnerID), find_root(mLoserID)  # root nodes 점수 변경.
    # 최상위 부모 노드에 값을 반영한다.
    scores[winner_root] += mScore
    scores[loser_root] -= mScore
    pass


def unionTeam(mPlayerA, mPlayerB):
    # 각 노드의 부모 노드를 찾는다.
    a, b = find_root(mPlayerA), find_root(mPlayerB)
    # 번호가 작은쪽의 노드에 부모 인덱스로 연결
    if a < b:
        # 더 큰 번호인 b의 부모를 a로 연결
        parents[b] = a
        # b의 스코어에 a와의 점수차이를 반영함 (추후 b의 스코어는 최상위 부모인 a까지 찾아가는 동안 +되어 최종 스코어를 계산)
        scores[b] -= scores[a]
    else:
        parents[a] = b
        scores[a] -= scores[b]

    # 최초에 4, 5번 노드가 Union되어 5번 값에 4번 값을 뺐음.
    # 이후 5, 1번 노드가 Union되어 5번 노드의 부모인 4번 노드에 부모를 1번 노드로 바꿔줌
    # 그리고 4번 노드의 스코어에 1번 노드의 값을 뺌.
    # 결과적으로 5번 노드는(-75) 4번 들어가서 + (-75+-50 = -125) -> 1번 들어가서 +해서 최종값 계산 (-125+50 = -75)
    # updatescore(5, 6, 75)를 해줘서 5번 노드의 값이 0이 됨. (그림 확인)

    """
    // A  점수를 기준으로  B 점수 보정 
     //  예)  A:10점 , B:20점 일때   B 가  A 로 합쳐 질때  조 대표는  A가 된다. 
     // A 는 그대로 10점으로 가지고  B 의 점수는  20-10 =10  점으로 보정한다. 
     // B 점수를 확인할 때  B  점수 +  조대표(A)점수가  B 의 점수이다. 
     // B 의 경우   parent id 가 A 로 되어 있기 때문에 점수 계산이 가능하다.
     """
    pass


def getScore(mID):
    # mID 노드의 현재 스코어에 최상위 부모 노드까지 찾아가며 값을 +하여 점수를 더함.
    cur_score = scores[mID]
    while (1):  # 부모 노드에 도달할때까지 연쇄적으로 부모 노드의 점수 더함. (루트 점수까지 더하면 stop)
        if mID == parents[mID]:
            return cur_score
        mID = parents[mID]
        cur_score += scores[mID]
    return 0


def find_root(node):
    while (1):
        # 노드가 부모 노드와 같으면 촤상위 부모 노드를 찾은거임.
        if node == parents[node]:
            return node
        # 노드에 부모노드번호를 반영함
        node = parents[node]