from collections import defaultdict
from heapq import heappush, heappop


def init(N):
    global empty_space, empty_list, Id_dict
    empty_space = N
    empty_list = []
    heappush(empty_list, (1, N))
    Id_dict = defaultdict(list)
    return


def add(mId, mSize):
    global empty_space, empty_list, Id_dict
    if mSize > empty_space:
        return -1
    empty_space -= mSize
    while mSize > 0:
        start, end = heappop(empty_list)
        empty_size = end - start + 1
        if mSize <= empty_size:                                 # msize 42, empty_size 2. 출근길 라디오
            heappush(Id_dict[mId], (start, start + mSize -1))
            if start + mSize -1 < end:                          # empty_list 조각에서 Id_dict에 push한 후 남은 공간이 있는지 check
                heappush(empty_list, (start + mSize, end))
            else:
                pass
            mSize = 0
            break
        else:
            mSize = mSize - empty_size
            heappush(Id_dict[mId], (start, end))
    return Id_dict[mId][0][0]


def remove(mId):
    global empty_space, empty_list, Id_dict
    count = 0
    while Id_dict[mId]:
        start, end = heappop(Id_dict[mId])
        empty_space += end-start+1
        heappush(empty_list, (start, end))
        empty_list = update_empty_list()
        count += 1
    if Id_dict[mId] != 0:
        del Id_dict[mId]
    return count

def update_empty_list():
    global empty_space, empty_list, Id_dict
    res = []
    while len(empty_list) > 0:
        start, end = heappop(empty_list)
        if len(res) != 0 and res[-1][1] +1 == start:            # start 1, end 3, mstart 4, mend 10
            res[-1] = (res[-1][0], end)
        else:
            heappush(res, (start,end))
    return res

def count(mStart, mEnd):
    global empty_space, empty_list, Id_dict
    count = 0
    for key in Id_dict:
        for start, end in Id_dict[key]:
            if end < mStart or mEnd < start:
                continue
            else:
                count += 1
                break
    return count