from collections import defaultdict


def init(N: int, M: int, mType: list, mTime: list) -> None:
    global load_time, sqrt, sqrt_time, load_type, sqprt_time
    load_time = [0] * N
    sqrt = 320
    sqrt_time = [0] * sqrt
    load_type = defaultdict(list)
    for i in range(N):
        load_time[i] = mTime[i]
        load_type[mType[i]].append(i)
        sqrt_time[i//sqrt] += mTime[i]
    return


def destroy() -> None:
    return


def update(mID: int, mNewTime: int) -> None:
    global load_time, sqrt, sqrt_time, load_type, sqprt_time
    sqrt_time[mID//sqrt] += mNewTime - load_time[mID]
    load_time[mID] = mNewTime
    return


def updateByType(mTypeID: int, mRatio256: int) -> int:
    global load_time, sqrt, sqrt_time, load_type, sqprt_time
    res = 0
    for index in load_type[mTypeID]:
        update(index ,int((load_time[index] * mRatio256) / 256))
        res += load_time[index]
    return res


def calculate(mA: int, mB: int) -> int:
    global load_time, sqrt, sqrt_time, load_type, sqprt_time
    if mA > mB : mA , mB = mB, mA
    res = 0
    left = mA
    right = mB -1                      # 3~4까지라면 3번의 구간만 더해야해서 -1

    while left <= right and left%sqrt:  # left부터 319까지 더하기
        res += load_time[left]
        left += 1

    while left <= right and (right + 1) % sqrt: # right부터 320까지 더하기
        res += load_time[right]
        right -= 1

    while left <= right:
        res += sqrt_time[left//sqrt]
        left += sqrt
    # left 112이고 mB 648이라면, 321~640구간을 더하고 종료하여야함. 그 구간은 몫이 1인 구간
    # left가 320까지 +되며 더해졌고 left값 = 320됨, left를 sqrt로 나눈 몫이 1인 sqrt_time 구간을 더함
    # right가 640까지 +되며 더해져 right값 = 640됨
    # sqrt_time구간을 더하고 left에 sqrt를 더하면 그 다움구간을 더함
    return res