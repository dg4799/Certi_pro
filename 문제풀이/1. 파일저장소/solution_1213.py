"""
빈공간이 주어지고 빈공간에 mID의 파일을 추가할 수 있다.
파일의 크기보다 남은 빈공간이 작으면 파일을 쪼개서 넣어야 함.

- init
  1. heap에 빈공간을 push함

- add
  1. empty_size보다 mSize가 크면
    - return -1

  2. 작으면
    - empty_size보다 -= mSize 후 while을 돌림
    - heap에서 empty_space를 꺼냄 (1, N+1)

  3. empty_space보다 mSize가 작으면 --> 저장공간에 한번에 넣을 수 있으면
    - empty_space의 start지점을 mSize 만큼 늘림 (mSize +1, N+1)
    - heap에 다시 empty_space를 넣음 --> 빈공간이 쪼개져 있을 수 있기 때문에 heap에 저장함
    - save_storage[mID].append(start, end)를 넣음
    - 최조 저장인지 check -> return에 최초 저장의 start값 반환
    * 파일을 저장할 빈공간이 부족하면 -1 return

  4. empty_space보다 mSize가 크면
    - mSize를 empty_space만큼 자른다
    - 자르고 남은만큼 save_storage에 저장함
    - save_storage[mID].append(start, end)를 넣음

- remove
  0. save_storage[mID]의 값만큼 empty_space에 += 하고 count
  1. save_storage의 mID를 삭제
  2. count를 return

- count
  0. count_set을 만든다
  1. save_storage를 가지고 카운트를 해야하는데..
  2. ([mID][0], [mID][1]) -> [mID][1] < mStrat  --> break
                             mEnd < [mID][0] --> break
  3. count_set에 mID를 저장
  4. count_set 갯수를 return

"""

from collections import defaultdict
from heapq import heappop, heappush


def init(N):
    global empty_space, empty_size, save_storage
    """
    - init
  1. heap에 빈공간을 push함
    """
    empty_space = [(1, N)]
    empty_size = N
    save_storage = defaultdict(list)


def add(mId, mSize):
    """
    - add
  1. empty_size보다 mSize가 크면
    - return -1

  2. 작으면
    - empty_size보다 -= mSize 후 while을 돌림
    - heap에서 empty_space를 꺼냄 (1, N+1)

  3. empty_space보다 mSize가 작으면 --> 저장공간에 한번에 넣을 수 있으면
    - empty_space의 start지점을 mSize 만큼 늘림 (mSize +1, N+1)
    - heap에 다시 empty_space를 넣음 --> 빈공간이 쪼개져 있을 수 있기 때문에 heap에 저장함
    - save_storage[mID].append(start, end)를 넣음
    - 최조 저장인지 check -> return에 최초 저장의 start값 반환
    * 파일을 저장할 빈공간이 부족하면 -1 return

  4. empty_space보다 mSize가 크면
    - mSize를 empty_space만큼 자른다
    - 자르고 남은만큼 save_storage에 저장함
    - save_storage[mID].append(start, end)를 넣음

    """
    global empty_space, empty_size, save_storage

    if empty_size < mSize:
        return -1

    empty_size -= mSize
    start_add = 0
    while mSize:
        (start, end) = heappop(empty_space)

        if end - start + 1 >= mSize:
            save_storage[mId].append((start, start + mSize - 1))
            if start_add == 0:
                start_add = start
            start, end = start + mSize, end
            if start > end:
                pass
            else:
                heappush(empty_space, (start, end))
            mSize = 0
        else:
            mSize -= end - start + 1
            save_storage[mId].append((start, end))
            if start_add == 0:
                start_add = start

    return start_add


def remove(mId):
    """
    - remove
  0. save_storage[mID]의 값만큼 empty_space에 += 하고 count
  1. save_storage의 mID를 삭제
  2. count를 return
    """
    count = 0
    global empty_space, empty_size, save_storage
    for value in save_storage[mId]:
        empty_size += (value[1] - value[0]) + 1
        heappush(empty_space, (value[0], value[1]))
        count += 1
    empty_space = update_empty_list()
    del save_storage[mId]

    return count


def update_empty_list():
    global empty_space
    res = []
    while empty_space:
        start, end = heappop(empty_space)

        if len(res) != 0 and res[-1][1] + 1 == start:  # start 1, end 3, mstart 4, mend 10
            res[-1] = (res[-1][0], end)
        else:
            heappush(res, (start, end))
    return res


def count(mStart, mEnd):
    """
    - count
  0. count_set을 만든다
  1. save_storage를 가지고 카운트를 해야하는데..
  2. ([mID][0], [mID][1]) -> [mID][1] < mStrat  --> break
                             mEnd < [mID][0] --> break
  3. count_set에 mID를 저장
  4. count_set 갯수를 return
    """
    count_set = set()
    global empty_space, empty_size, save_storage
    for key in save_storage:
        for value in save_storage[key]:
            if value[1] < mStart: continue
            if mEnd < value[0]: continue
            count_set.add(key)

    return len(count_set)