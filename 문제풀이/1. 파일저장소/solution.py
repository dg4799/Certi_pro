from heapq import heappush, heappop
from collections import defaultdict

def init(N):
    global empty_space, empty_list, Id_dict
    empty_list = []
    heappush(empty_list, (1, N))
    empty_space = N
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
        if empty_size >= mSize:
            heappush(Id_dict[mId], (start, start + mSize - 1))
            start += mSize
            if start <= end:
                heappush(empty_list, (start, end))
            mSize = 0
            break
        else:
            mSize -= empty_size
            heappush(Id_dict[mId], (start, end))
    return Id_dict[mId][0][0]





def remove(mId):
    global empty_space, empty_list, Id_dict
    cnt = len(Id_dict[mId])
    while Id_dict[mId]:
        start, end = heappop(Id_dict[mId])
        heappush(empty_list, (start, end))
        empty_space += end - start + 1
    del Id_dict[mId]
    empty_list = update_empty_list()
    return cnt



def update_empty_list():
    global empty_list
    res = []
    while empty_list:
        start, end = heappop(empty_list)
        if res and res[-1][1] + 1 == start:
            res[-1] = (res[-1][0], end)
        else:
            res.append((start, end))
    return res

def count(mStart, mEnd):
    global Id_dict
    count = 0
    for key in Id_dict:
        for start, end in Id_dict[key]:
            if end < mStart or start > mEnd:
                continue
            else:
                count += 1
                break
    return count