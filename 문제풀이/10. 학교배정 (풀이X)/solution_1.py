from collections import defaultdict
from heapq import heappop, heappush


def init(stud, sch, mX, mY):
    global C, N, studSchOrder, studAssigned, studMaxdist, removed, schCapa, schStudList, schWaitList, schLoc

    C, N = stud, sch
    studSchOrder = defaultdict(list)
    studAssigned = defaultdict(int)
    studMaxdist = defaultdict(int)
    removed = set()
    schCapa = [C] * N
    schStudList = [[] for _ in range(N)]
    schWaitList = [[] for _ in range(N)]
    schLoc = []
    for x, y in zip(mX, mY):
        schLoc.append((x, y))


def assign(mStudent, maxDist):
    studID, dist = mStudent, maxDist
    while True:
        studAssigned[studID] += 1
        sch = studSchOrder[studID][studAssigned[studID]]
        if mStudent == studID:
            ans = sch
        heappush(schStudList[sch], (dist, -studID))
        if len(schStudList[sch]) <= schCapa[sch]:
            return ans
        while True:
            dist, studID = heappop(schStudList[sch])
            studID = -studID
            if (studID, dist) not in removed and studSchOrder[studID][studAssigned[studID]] == sch:
                break
            schCapa[sch] -= 1
            # if (studID, dist) in removed:
            #     removed.pop((studID, dist))
        heappush(schWaitList[sch], (-dist, studID))


def add(mStudent, mX, mY):
    toDist = []
    for i in range(N):
        toDist.append((abs(mX - schLoc[i][0]) + abs(mY - schLoc[i][1]), i))
    toDist.sort()
    studSchOrder[mStudent] = [i for _, i in toDist]
    studAssigned[mStudent] = -1
    studMaxdist[mStudent] = toDist[-1][0]

    return assign(mStudent, toDist[-1][0])


def remove(mStudent):
    sch = studSchOrder[mStudent][studAssigned[mStudent]]
    studSchOrder[mStudent] = []
    studAssigned[mStudent] = -1
    dist = studMaxdist[mStudent]
    removed.add((mStudent, dist))
    ans = sch
    schCapa[sch] += 1
    while schWaitList[sch]:
        dist, studID = heappop(schWaitList[sch])
        dist = -dist
        if (studID, dist) in removed:
            continue
        now_sch = studSchOrder[studID][studAssigned[studID]]
        schCapa[now_sch] += 1
        while True:
            if studSchOrder[studID][studAssigned[studID]] == sch:
                break
            studAssigned[studID] -= 1
        heappush(schStudList[sch], (dist, -studID))
        sch = now_sch

    return ans


def status(mSchool):
    return len(schStudList[mSchool]) - (schCapa[mSchool] - C)