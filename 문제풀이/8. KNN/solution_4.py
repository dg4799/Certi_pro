from collections import defaultdict
from heapq import heappop, heappush


def init(K: int, L: int) -> None:
    global k, l, locDict, neighborDict
    k = K
    l = L
    neighborDict = defaultdict(list)  ## { (mX//l, mY//y) : [(mX,mY,mC,mID),~] , ~  }
    locDict = defaultdict(tuple)  ## { mID : (mX//l, mY//y,mX,mY,mC) , ~  }


def addSample(mID: int, mX: int, mY: int, mC: int) -> None:

    # (mX, mY)의 포인트를 l로 나눈 구간에 모으기 위해 nX, nY를 만든다
    # 추후 어떤지점 (pX, pY)가 주어졌을때 (pX, pY)가 속한 구간을 찾고
    # 그 구간에서 dX= [-1, 0, 1], dY = [-1, 0, 1]를 돌려 주변 구간에서의 포인트를 체크한다
    #  - 구간의 크기가 l 단위인 구간만 체크하면 됨, l 이상 크기(2~)의 구간은 전부 이상치이므로 체크할 필요 없음!
    # 이때 일부 l보다 멀리 있는 이상치 데이터가 있을 수 있음
    nX = mX // l
    nY = mY // l

    # 구간 정보 dict에 정보를 집어 넣음
    neighborDict[(nX, nY)].append((mX, mY, mC, mID))
    # delete는 mID를 받아서 하기 때문에
    # mID에 해당되는 값들을 빠르게 찾기위해 [mID]에 정보를 집어넣음
    locDict[mID] = (nX, nY, mX, mY, mC)


def deleteSample(mID: int) -> None:
    # mID에 해당되는 정보를 꺼내서
    nX, nY, mX, mY, mC = locDict[mID]
    # 구간정보 dict에서 해당 정보를 지운다
    neighborDict[(nX, nY)].remove((mX, mY, mC, mID))
    # 그리고 mID도 삭제
    del locDict[mID]


def predict(pX: int, pY: int) -> int:

    # 특정 위치인 (pX, pY)의 구간을 계산하고
    nX = pX // l
    nY = pY // l

    # 최근접 이웃을 찾아 담기위한 리스트 생성
    resultList = []

    # (pX, pY)가 속한 구간에서 주변 구간을 모두 돌며 체크하기 위해 dX, dY를 for문으로 돌림
    for dX in [-1, 0, 1]:
        for dY in [-1, 0, 1]:
            # 구간정보dict에서 pX, pY의 구간인 nX, nY에 dX, dY를 더해 해당 구간에서 값을 빼온다
            for neighbor in neighborDict[(nX + dX, nY + dY)]:
                # 해당 구간에 속한 포인트의 값과 pX, pY의 값의 차를 구하여 dist를 계산
                dist = abs(pX - neighbor[0]) + abs(pY - neighbor[1])
                # dist가 l보다 작으면 resultList에 push (근접 이웃)
                if dist <= l:
                    heappush(resultList, (dist, neighbor[0], neighbor[1], neighbor[2]))
    # 최근접 이웃 k보다 resultList의 갯수가 작을경우 -1 반환
    result = -1
    if len(resultList) < k:
        return result

    # resultList에서 color 리스트를 heappop으로 뽑는다. (거리가 가장 낮은것들 순서임)
    # color가 최대 10개
    cList = [0] * 11
    for _ in range(k):
        _, _, _, c = heappop(resultList)
        # 인덱스별로 color 값을 뽑아 넣음
        cList[c] += 1

    maxVal = 0
    # 최대 10개인 color 종류를 모두체크해서 갯수가 가장 많은것 뽑음
    for i in range(1, 11):
        if cList[i] > maxVal:
            maxVal = cList[i]
            result = i

    return result