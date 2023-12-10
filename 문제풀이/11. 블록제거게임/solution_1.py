from heapq import heappush, heappop

def init(R: int, C: int) -> None:
    global numRow, numCol, blocks, totalCnt
    numRow = R
    numCol = C
    blocks = []  ## [(time,start,length,end)]
    totalCnt = 0
    pass


def dropBlocks(mTimestamp: int, mCol: int, mLen: int) -> int:
    global totalCnt
    # blocks 리스트에 시간, 위치, 길이, 위치+길이를 저장
    heappush(blocks, (mTimestamp, mCol, mLen, mCol + mLen))
    # 토탈카운트에 갯수를 +
    totalCnt += mLen

    # mTimestamp에 해당되는 blocks이 있다면? (업데이트로 따로 빼기)
    # blocks의 생성시각 + Row 행수가 mTimestamp보다 같거나 작으면 이미 지나감! 핵심!!!!!!!!
    while blocks[0][0] + numRow <= mTimestamp:  # 지나간 것 제거
        # heap에서 빼내서 토탈카운트에서 총 블록 제거
        totalCnt -= heappop(blocks)[2]  # 총 블록에서도 제거
    return totalCnt


def removeBlocks(mTimestamp: int) -> int:
    global blocks, totalCnt

    # 지나간 블럭은 haeap에서 빼냄
    while blocks and blocks[0][0] + numRow <= mTimestamp:  # 지나간 것 제거
        heappop(blocks)

    chkList = [0] * numCol  # 열 순차 탐색
    tmpBlock = []  # 제거 후 남은 블록
    tmpCnt = 0  # 제거 후 남은 블록 수

    # block을 하나씩 빼내어서 겹침을 체크해서 겹쳐진 블록만 남기기!!! 핵심!!!! (문제에서 글로 설명은 없지만 변화되는 그림에서는 유추 가능함)
    while blocks:
        t, st, len, end = heappop(blocks)
        tmpLen = 0
        # 꺼낸 블록을 열 방향으로 체크리스트에 있는지 확인 (이미 있으면 겹치는 구간)
        for i in range(st, end):
            # 꺼낸 블록이 겹치는 블록이라면
            if chkList[i] == 1:
                # 블록 겹침이 시작되는 구간을 체크
                if tmpLen == 0:
                    # 겸치는 블록의 시작지점을 저장 (추후 여기에 겹치는 수만큼 길이가됌)
                    newSt = i
                # 겹침 길이에 추가
                tmpLen += 1
            else:
                # 겹치지 않으면 해당칸에 블록이 있는것으로 처리
                chkList[i] = 1
                # 겹치지 않았으면 겹치는 길이를 마무리하기 위해 체크
                if tmpLen > 0:
                    # 임시 카운트에 겹친 길이만큼 추가
                    tmpCnt += tmpLen
                    # 임시 블록 리스트에 겹친 블록을 넣음
                    heappush(tmpBlock, (t, newSt, tmpLen, newSt + tmpLen))
                    # 겹친 길이 초기화 (마무리)
                    tmpLen = 0

            # for문의 끝이 end까지 이므로 마지막에서 겹쳐진 부분을 마무리
            if i == end - 1 and tmpLen > 0:
                # 임시블록 리스트에 넣음
                tmpCnt += tmpLen
                heappush(tmpBlock, (t, newSt, tmpLen, newSt + tmpLen))
                tmpLen = 0
    # 블록리스트를 업데이트
    blocks = tmpBlock
    # 토탈카운트도 업데이트
    totalCnt = tmpCnt
    return totalCnt