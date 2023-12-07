from collections import defaultdict
from heapq import heappush, heappop

dx = [0, 1, -1]
dy = [0, 1, -1]

def init(K: int, L: int) -> None:
    global Point_list, del_mID, k, l
    Point_list = defaultdict(list)
    del_mID = defaultdict(list)
    k = K
    l = L
    pass


def addSample(mID: int, mX: int, mY: int, mC: int) -> None:
    nX = mX // l
    nY = mY // l
    # Point_list[(nX, nY)] = (mX, mY, mC, mID)
    Point_list[(nX, nY)].append((mX, mY, mC, mID))
    del_mID[mID] = (nX, nY, mX, mY, mC)


def deleteSample(mID: int) -> None:
    (nX, nY, mX, mY, mC) = del_mID[mID]
    Point_list[(nX, nY)].remove((mX, mY, mC, mID))
    del del_mID[mID]

def predict(mX: int, mY: int) -> int:

    nX = mX // l
    nY = mY // l

    resultlist = []
    for i in dx:
        for j in dy:
            if (nX+i, nY+j) in Point_list:
                for h in Point_list[(nX+i, nY+j)]:
                    (cX, cY, mC, mID) = h
                    dist = abs(mX - cX) + abs(mY - cY)
                    if dist <= l: # 여기서 l보다 작은 것만 추가해서
                        heappush(resultlist, (dist, cX, cY, mC))

    if len(resultlist) < k: # resultlist의 갯수가 k보다 작으면 return -1, 왜냐하면 l이 넘는 구간의 것은 체크하지 않기 때문?
        return -1

    else:
        break_k = 0
        color = [0] * 11
        for i in range(len(resultlist)):
            (dist, mX, mY, mC) = heappop(resultlist)
            color[mC] += 1
            break_k += 1
            if break_k == k:
                break

        res = 0
        maxVal = 0
        for j in range(11):
            if maxVal < color[j]:
                maxVal = color[j]
                res = j
    # print(res)
    return res