from collections import defaultdict

sq = 320  # N 제곱근보다 커야 함 #N<=100,000


def init(N: int, M: int, mType: list, mTime: list):
    global n, m, road_time, type_road, sq_time
    n = N  # max 100,000
    m = M  # max 1000
    road_time = [0] * N
    sq_time = [0] * sq                                                      # 구간합을 구하기 위함. N=100,000의 제곱근인 316보다 큰 320으로 구간 개수를 잡음
    type_road = defaultdict(list)
    for i in range(N):
        road_time[i] = mTime[i]  # 구간별 시간
        type_road[mType[i]].append(i)  # {타입: [구간, 구간, 구간], ...}
        sq_time[i // sq] += mTime[i]  # 320개 구간마다 시간 합 저장            # i를 sq로 나누면 몫이나오는데 0~320 = 0, 321~640 = 1 이렇게 320마다 sq_time 인덱스에 접근
                                                                           # 0번 구간에 mTime을 모두 더하고 .... 해서 320 구간까지 합을 모두 더해둠
                                                                           # calcu에서 구간합을이용해 합산을 빠르게함.


def destroy():
    pass


def update(mID: int, mNewTime: int):
    sq_time[mID // sq] += mNewTime - road_time[mID]  # 해당 구간 시간 업데이트    # 구간합의 시간에도 업데이트되는 시간을 반영, 기존시간 50이고 업데이트시간 100이면,
    road_time[mID] = mNewTime                                                 # 50만큼 늘어나는거고 업데이트시간 100-기존시간50 해서 50을 sq_time에 더하면
                                                                              # 해당 구간의 합이 업데이트됨.

def updateByType(mTypeID: int, mRatio256: int) -> int:  # 최대 200회
    res = 0
    for r_id in type_road[mTypeID]:  # 최대 100K                              # 도로 종류의 인덱스만 뽑아서 update 시킴
        update(r_id, road_time[r_id] * mRatio256 // 256)
        res += road_time[r_id]
    return res


def calculate(mA: int, mB: int):  # 최대 100K 호출
    if mA > mB:                                                               # mA=318, mb=642일때 좌측(left)~구간까지합, 구간~우측(right)까지합에 구간합을 더함
        mA, mB = mB, mA                                                       # ex) 318 + 319 + 0~320 + 320~640 + 641 + 642
    res = 0
    l = mA
    r = mB - 1                                                                 # % = 나머지, 320으로 나누면 320일때 0, 640일때 0..
    while l <= r and l % sq:  # l만 속한 sq 길이의 구간합  #최대 sq-1 반복          # 1은 1, 322은 2, 643은 3.. 각 구간에서의 카운트 가능
        res += road_time[l]                                                    # l을 늘려 sq로 나눈 나머지가 0(False)가 될때까지 while이 돌아가고 break
        l += 1                                                                 # l부터 구간까지(sq로 나눈 나머지가 0) 더하는 것임.
                                                                              # while이 break 될때까지 left의 값을 계속 더함

    while l <= r and (r + 1) % sq:  # r만 속한 sq 길이의 구간합  #최대 sq-1 반복    # r을 줄여 sq로 나눈 나머지가 0(False)가 될때까지 while이 돌아가고 break
        res += road_time[r]                                                    # while이 break 될때까지 right의 값을 계속 더함
        r -= 1
    while l <= r:  # l, r 사이지만 둘다 없는 구간합; 구간씩 건너 뛰면서 더함  #최대 N//sq 반복
        res += sq_time[l // sq]                                                # mA=0, mB=389이면 320~389는 r 구간, r의 값을 while로 더함, r이 줄어서 0(False)가되어 탈출
        l += sq                                                                # 탈츌 후 구간합 while로 들어옴, l을 sq로 나누어 0번째 구간의 합을 더함
    return res                                                                 # l값에 sq를 더해 r보다 큰수를 만들어 while을 나옴.