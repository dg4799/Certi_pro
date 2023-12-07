##########################################################################
# 코드 설명
##########################################################################
'''
import sys
from solution import init, add, distance, count

CMD_INIT     = 100
CMD_ADD      = 200
CMD_DISTANCE = 300
CMD_COUNT    = 400

def run():
    len = int(sys.stdin.readline())
    for i in range(len):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))
        if cmd == CMD_INIT:
            mName1 = str(next(inputs))
            mDay1 = int(next(inputs))
            init(mName1, mDay1)   # User Code 1
            ret_val = 1
        elif cmd == CMD_ADD:
            mName1 = str(next(inputs))
            mName2 = str(next(inputs))
            mDay1 = int(next(inputs))
            mDay2 = int(next(inputs))
            ret = add(mName1, mName2, mDay1, mDay2)   # User Code 2
            ans = int(next(inputs))
            if ret != ans:
                ret_val = 0
        elif cmd == CMD_DISTANCE:
            mName1 = str(next(inputs))
            mName2 = str(next(inputs))
            ret = distance(mName1, mName2)   # User Code 3
            ans = int(next(inputs))
            if ret != ans:
                ret_val = 0
        elif cmd == CMD_COUNT:
            mDay1 = int(next(inputs))
            ret = count(mDay1)   # User Code 4
            ans = int(next(inputs))
            if ret != ans:
                ret_val = 0
    return ret_val

if __name__ == '__main__':
    # sys.stdin = open('sample_input.txt', 'r')   # 입력 파일 저장 → f = sys.stdin.readline() 사용 가능
    inputarray = input().split()   # 첫 줄 : TC , MARK   [예] 25, 100
    TC = int(inputarray[0])
    MARK = int(inputarray[1])
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0   # User Code 실행 후, 정답 확인 → MARK vs 0
        print("#%d %d" % (testcase, score), flush=True)
'''
##########################################################################
# 문제
##########################################################################
import bisect


# bisect : 이진 검색 알고리즘을 이용하여 입력받은 시퀀스를 검색하는 기능
# bisect.bisect(a, x, lo=0, hi=len(a)) # 리스트 a에 x값이 들어갈 자리의 인덱스값을 반환
# bisect_right (=bisect) , bisect_left : 동일한 값 존재하면 동일한 값 반환
# insort : 정렬된 시퀀스 a 에 x 값 삽입 (right, left 내용은 동일)

def init(mAncestor: str, mDeathDay: int) -> None:
    # mAncestor : 선조의 이름 ( 3 ≤ |mAncestor| ≤ 11, |A|는 A 문자열의 길이를 의미한다 )
    # mLastday : 선조의 마지막 생존일 ( 0 ≤ mLastDay ≤ 1,000,000 )

    global info_dict, parents, depths, birth, death, idx
    info_dict = {}
    # 선조 인덱스 0
    idx = 0
    info_dict[mAncestor] = idx
    parents = [idx]
    depths = [idx]
    birth = [idx]
    death = [mDeathDay]
    return


# idx 에 해당하는 리스트들     [예] idx =1 이면, 첫 add 로 추가된 자손에 대한  정보 → parents[1] , depths[1], birth[1], death [1]
# 자료 저장하면서 관계 저장 → 딕셔너리 활용

def add(mName: str, mParent: str, mBirthday: int, mDeathDay: int) -> int:
    # mName: 개체의 이름 ( 3 ≤ |mName| ≤ 11 )
    # mParent: 개체의 부모의 이름 ( 3 ≤ |mParent| ≤ 11 )
    # mFirstday: 개체의 첫 생존일 ( 부모의 Firstday ≤ mFirstday ≤ 부모의 Lastday )
    # mLastday: 개체의 마지막 생존일 ( mFirstday ≤ mLastday ≤ 1,000,000 )

    global info_dict, parents, depths, birth, death, idx

    # 입력받는 순서대로 인덱스로 이름을 부여함 (선조는 0, init에서 넣었음)
    idx += 1  # 리스트 내 인덱스 = 해당 이름
    # 이름 : 현재 인덱스를 저장 (idx 3일때 info_dict[이름] = 3)
    info_dict[mName] = idx  # info_dict[이름] = idx
    # 현재 인덱스의 부모 인덱스 번호 찾기
    pidx = info_dict[mParent]  # 부모 idx 탐색   [참고] 이전에 지정 : init | add
    # parents에 현재 인덱스의 부모 인덱스를 리스트에 넣기 (idx 3일때 partens[3] = 부모 인덱스)
    parents.append(pidx)  # 부모 리스트
    # 선조의 가계도 거리 추가 (idx 3일때 depths[3] = 현재 부모의 선조와의 거리 + 1(부모와의 거리)
    depths.append(depths[pidx] + 1)  # depth 에 부모 depth + 1

    # 입력 날짜 탐색 : birth 오른쪽 (날짜 이전 탄생 수) - death 왼쪽 (날짜 이전 죽음 수)
    # [예] 700 이면, birth 700 이하 갯수 - death 700 미만 갯수 (전에 죽음)
    bisect.insort_right(birth, mBirthday)  # birth 리스트에 입력값 삽입
    bisect.insort_right(death, mDeathDay)  # death 리스트에 입력값 삽입
    return depths[idx]


def distance(mName1: str, mName2: str) -> int:
    # mName1, mName2: 가계도 거리를 알아내려는 두 개체의 이름 ( 3 ≤ |mName1|, |mName2| ≤ 11 )

    global info_dict, parents, depths
    # nName1의 인덱스
    idx1 = info_dict[mName1]
    # nName2의 인덱스
    idx2 = info_dict[mName2]



    # 여기가 LCA 알고리즘임!!!

    # idx1의 깊이가 더 크다면
    # idx2를 더 크게 설정
    if depths[idx1] > depths[idx2]:  # 깊이 : idx1 < idx2 설정
        tmp = idx1
        idx1 = idx2
        idx2 = tmp
    res = 0
    # 깊이가 서로 다르다면
    while depths[idx1] != depths[idx2]:  # 깊이가 다르면
        # 깊이가 큰쪽(idx2)의 인덱스를 부모로 인덱스로 바꾸고 거리+1 --> 한칸 올라감
        idx2 = parents[idx2]  # 깊은 idx 한 칸 위로(부모) → 거리 + 1
        res += 1
    # 같은 조상이 아니라면
    while idx1 != idx2:
        # 노드가 같아질때까지 인덱스를 부모로 인덱스로 바꾸고 거리+1
        idx1 = parents[idx1]  # 한 칸 위로 → 거리 + 1
        idx2 = parents[idx2]  # 한 칸 위로 → 거리 + 1
        res += 2
    return res


def count(mDay: int) -> int:
    # mDay: 생존한 개체 수를 조사하는 날짜 ( 0 ≤ mDay ≤ 1,000,000 )

    global birth, death
    # 입력 날짜 탐색 : birth 오른쪽 (날짜 이전 탄생 수) - death 왼쪽 (날짜 이전 죽음 수)
    # [예] 700 이면, birth 700 이하 갯수 - death 700 미만 갯수 (전에 죽음)
    b_right = bisect.bisect_right(birth, mDay)
    b_left = bisect.bisect_left(death, mDay)
    res = b_right - b_left
    return res


##########################################################################
# 문제
##########################################################################
'''
def init(mAncestor:str, mDeathDay:int) -> None:
    return
def add(mName:str, mParent:str, mBirthday:int, mDeathDay:int)-> int:
    return 0
def distance(mName1:str, mName2:str)-> int:
    return 0
def count(mDay:int) -> int:
    return 0
'''