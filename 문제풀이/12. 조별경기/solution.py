"""
조별경기 과제
- Union find를 응용해서 해당 조에 값을 반영시킴
- Union find는 인덱스번호가 작은쪽을 부모로 연결시키고 값을 빼주어 추후에 최상위 노드까지 타고올라가며 최종값을 계산함

- UpdateScore
  1. mWinnerID, mLoserID의 최상위 부모노드를 찾는다
  2. mScore를 각각 ID에 반영

- unionTeam
  1. mPlayerA, mPlayerB의 최상위 부모노드를 찾는다
  2. 부모노드의 인덱스가 작은쪽의 인덱스를 큰쪽의 인덱스에 부모노드로 넣는다.
  3. 부모노드의 값의 차이만큼 빼준다.

- getScore
  1. 입력받은 mID가 부모노드와 같은지 체크하고 아니라면 mID에 부모노드값을 넣는다.
  2. 부모노드와 같아질때까지 돌리면서 score를 += 해주면 해당 mID가 최상위 노드까지 가면서 최종값을 계산할 수 있음!

- getFindParent
  1. mID를 입력받고 부모노드와 같은지 체크하고 같으면 return
  2. 아니라면 mID에 부모노드값을 넣고 다시 돌림

"""



def init(N):
    global scores, parent
    scores = [0] * (N + 1)
    parent = list(range(N + 1))
    # parent = [i for i in range(0, N+1)]
    # scores = [0 for i in range(0, N+1)]
    pass


def updateScore(mWinnerID, mLoserID, mScore):
    """
    - UpdateScore
  1. mWinnerID, mLoserID의 최상위 부모노드를 찾는다
  2. mScore를 각각 ID에 반영
    """
    global scores

    WinnerID = getFindParent(mWinnerID)
    LoserID = getFindParent(mLoserID)
    scores[WinnerID] += mScore
    scores[LoserID] -= mScore
    pass


def unionTeam(mPlayerA, mPlayerB):
    """
    - unionTeam
  1. mPlayerA, mPlayerB의 최상위 부모노드를 찾는다
  2. 부모노드의 인덱스가 작은쪽의 인덱스를 큰쪽의 인덱스에 부모노드로 넣는다.
  3. 부모노드의 값의 차이만큼 빼준다.
    """
    global parent, scores

    node_a = getFindParent(mPlayerA)
    node_b = getFindParent(mPlayerB)

    if node_a < node_b:
        parent[node_b] = node_a
        scores[node_b] -= scores[node_a]
    else:
        parent[node_a] = node_b
        scores[node_a] -= scores[node_b]


def getScore(mID):
    """
    - getScore
  1. 입력받은 mID가 부모노드와 같은지 체크하고 아니라면 mID에 부모노드값을 넣는다.
  2. 부모노드와 같아질때까지 돌리면서 score를 += 해주면 해당 mID가 최상위 노드까지 가면서 최종값을 계산할 수 있음!
    """
    global scores, parent
    current_score = scores[mID]

    while True:
        if mID == parent[mID]:
            return current_score
        mID = parent[mID]
        current_score += scores[mID]


def getFindParent(mID):
    global parent
    """
    - getFindParent
  1. mID를 입력받고 부모노드와 같은지 체크하고 같으면 return
  2. 아니라면 mID에 부모노드값을 넣고 다시 돌림
    """
    while True:
        if mID == parent[mID]:
            return mID
        mID = parent[mID]