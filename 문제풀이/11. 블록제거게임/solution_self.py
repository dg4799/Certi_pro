from heapq import heappush, heappop


def init(R: int, C: int) -> None:
    global mRow, mCol, block_list, totalcount
    mRow = R
    mCol = C
    block_list = []
    totalcount = 0
    return


def update(mTimestamp):
    global block_list, mRow, totalcount

    while block_list and block_list[0][0] + mRow <= mTimestamp:
        _, _, mLen = heappop(block_list)
        totalcount -= mLen


def dropBlocks(mTimestamp: int, mCol: int, mLen: int) -> int:
    global block_list, totalcount

    update(mTimestamp)
    heappush(block_list, (mTimestamp, mCol, mLen))
    totalcount += mLen

    return totalcount


def removeBlocks(mTimestamp: int) -> int:
    global mCol, block_list, totalcount

    update(mTimestamp)

    Col_list = [0 for i in range(mCol)]
    tmp_count = 0
    tmp_start = 0
    tmp_len = 0
    tmp_block = []
    while block_list:
        Time, Col, Len = heappop(block_list)
        for i in range(Col, Col + Len):
            if Col_list[i] == 0:
                if tmp_len > 0:
                    heappush(tmp_block, (Time, tmp_start, tmp_len))
                    tmp_count += tmp_len
                    tmp_start = 0
                    tmp_len = 0
                Col_list[i] = 1
            else:
                if tmp_start == 0:
                    tmp_start = i
                tmp_len += 1

                if i == Col + Len - 1:
                    heappush(tmp_block, (Time, tmp_start, tmp_len))
                    tmp_count += tmp_len
                    tmp_start = 0
                    tmp_len = 0
    block_list = tmp_block
    totalcount = tmp_count

    return totalcount