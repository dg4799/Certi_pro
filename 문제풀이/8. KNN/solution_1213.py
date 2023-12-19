"""
- l을 초과하는 자료형은 이상치로 추정 (sqrt 2차원 기준값을 l로 설정)
- 값이 많은 색상을 범주로 return
- 붉은색 2개, 파란색 2개가 있으면 가장 작은값을 가지는 범주로 추정(같은 값이 있을때 작은값을 범주로 return)

- init
1. sqrt[]를 만든다. -> 4000개


- deleteSample
1. 자료를 삭제하지않고 delete list에 mID를 넣는다.
2. 이후 predict에서 체크할때 delete list에 포함된 mID는 continue


"""

from collections import defaultdict
from heapq import heappop, heappush


def init(K: int, L: int) -> None:
    """
    - init
1. sqrt[]를 만든다. -> 4000개
    """
    global sqrt_list, l, k, delete_list, dx, dy
    l = L
    k = K
    sqrt_list = defaultdict(list)
    # delete_list = set()
    delete_list = defaultdict(list)
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]


def addSample(mID: int, mX: int, mY: int, mC: int) -> None:
    """
    - addSample
1. mX, mY를 받아 l의 몫을 구해 sqrt 구간을 찾음
2. sqrt[구간].append(mID, mX, mY, mC)를 넣음
    """
    nX = mX // l
    nY = mY // l
    sqrt_list[(nX, nY)].append((mID, mX, mY, mC))
    delete_list[mID] = (nX, nY, mX, mY, mC)


def deleteSample(mID: int) -> None:
    (nX, nY, mX, mY, mC) = delete_list[mID]
    sqrt_list[(nX, nY)].remove((mID, mX, mY, mC))
    del delete_list[mID]


def predict(mX: int, mY: int) -> int:
    """
    - predict
1. mX, mY를 받아 sqrt 구간을 찾음
2. dx, dy로 8개 방향의 구간을 꺼냄
3. 해당 구간에 포함된 자료들을 꺼냄
4. distance를 계산해서 heap에 push

5. K 값만큼 for 문을 돌림
6. heap에서 distance를 꺼냄
7. mC리스트에 인덱스에 mC갯수를 += 해줌
8. mC리스트에서 가장값이 큰 인덱스를 return
  - [2, 2, 1, 0, 0, 0]
  - for문을 돌려서 MaxMC = -1을 갱신해서 return
    """
    pX = mX // l
    pY = mY // l

    distance_list = []
    for i in dx:
        for j in dy:
            nX = pX + i
            nY = pY + j
            if (nX, nY) in sqrt_list:
                for (mID, X, Y, mC) in sqrt_list[(nX, nY)]:
                    distance = abs(mX - X) + abs(mY - Y)
                    # if mID in delete_list: continue
                    if distance <= l:
                        heappush(distance_list, (distance, X, Y, mC))

    if len(distance_list) < k:
        return -1
    else:
        count = 0
        mC_list = [0] * 11
        while distance_list:
            distance, X, Y, mC = heappop(distance_list)
            mC_list[mC] += 1
            count += 1
            if count == k: break

        res = 0
        MaxValue = 0
        for i in range(1, 11):
            if mC_list[i] > MaxValue:
                MaxValue = mC_list[i]
                res = i
    return res


"""



"""