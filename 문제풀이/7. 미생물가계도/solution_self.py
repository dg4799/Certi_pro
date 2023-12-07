"""
init and and
입력받은 노드의 이름을 인덱스번호로 저장하는 리스트 만듬
해당인덱스의 부모인덱스를 저장하는 리스트를 만듬
깊이를 저장하는 리스트를 만듬
탄생 리스트와 죽음 리스트를 만들고 insort_right를 써서 값을 추가함 (정렬이 되게끔)

distance
입력받은 노드의 이름을 인덱스 번호를 찾아서
두번째 인덱스의 깊이가 더 깊도록 두 인덱스를 교차해주고
두 인덱스의 깊이를 체크해서 깊이가 같지 않으면 더 깊은 두번째 인덱스를 부모 인덱스로 바꾸고 거리 +1
그리고 다시 두 인덱스를 비교해서 조상이 같지 않으면
두 인덱스 각각 부모 인덱스로 바꾸고 거리 + 1씩

count
1. 탄생 리스트에서 bisect_right로 mDay를 체크(mDay를 포함하는 갯수)이내에 들어오는 갯수가 몇개인지 체크 --> mDay를 포함한 mDay 보다 낮은 값의 갯수
2. 죽음 리스트에서 bisect_left로 mDay를 체크(mDay에 해당되지 않으면 리스트 갯수 전체) 이내에 들어오는 갯수가 몇개인지 체크 --> mDayt를 미포함한 mDay보다 낮은 값의 갯수
해당 범위에 포함되는 갯수 = 1번 - 2번

"""
import bisect
from bisect import insort

def init(mAncestor:str, mDeathDay:int) -> None:
    """
    입력받은 노드의 이름을 인덱스번호로 저장하는 리스트 만듬
해당인덱스의 부모인덱스를 저장하는 리스트를 만듬
깊이를 저장하는 리스트를 만듬
탄생 리스트와 죽음 리스트를 만들고 insort_right를 써서 값을 추가함 (정렬이 되게끔)
    :param mAncestor: 조상
    :param mDeathDay: 죽음 일수
    :return:
    """
    global info_name, parent_list, depth_list, birth, die, idx
    idx = 0
    info_name = {}
    info_name[mAncestor] = idx
    parent_list = [idx]
    depth_list = [idx]
    birth = [0]
    die = [mDeathDay]
    return

def add(mName:str, mParent:str, mBirthday:int, mDeathDay:int)-> int:
    global idx
    idx += 1
    info_name[mName] = idx
    parent_list.append(info_name[mParent])
    depth_list.append(depth_list[info_name[mParent]]+1)
    insort(birth, mBirthday)
    insort(die, mDeathDay)

    return depth_list[info_name[mParent]]+1

def distance(mName1:str, mName2:str)-> int:
    """
    입력받은 노드의 이름을 인덱스 번호를 찾아서
두번째 인덱스의 깊이가 더 깊도록 두 인덱스를 교차해주고
두 인덱스의 깊이를 체크해서 깊이가 같지 않으면 더 깊은 두번째 인덱스를 부모 인덱스로 바꾸고 거리 +1
그리고 다시 두 인덱스를 비교해서 조상이 같지 않으면
두 인덱스 각각 부모 인덱스로 바꾸고 거리 + 1씩
    :param mName1:
    :param mName2:
    :return:
    """
    index_1 = info_name[mName1]
    index_2 = info_name[mName2]

    if depth_list[index_1] > depth_list[index_2]:
        index_1, index_2 = index_2, index_1

    res = 0
    while depth_list[index_1] != depth_list[index_2]:
        index_2 = parent_list[index_2]
        res += 1
    while index_1 != index_2:
        index_1 = parent_list[index_1]
        index_2 = parent_list[index_2]
        res += 2

    return res

def count(mDay:int) -> int:
    """
    count
1. 탄생 리스트에서 bisect_right로 mDay를 체크(mDay를 포함하는 갯수)이내에 들어오는 갯수가 몇개인지 체크 --> mDay를 포함한 mDay 보다 낮은 값의 갯수
2. 죽음 리스트에서 bisect_left로 mDay를 체크(mDay에 해당되지 않으면 리스트 갯수 전체) 이내에 들어오는 갯수가 몇개인지 체크 --> mDayt를 미포함한 mDay보다 낮은 값의 갯수
해당 범위에 포함되는 갯수 = 1번 - 2번
    :param mDay:
    :return:
    """

    birth_count = bisect.bisect_right(birth, mDay)
    die_count = bisect.bisect_left(die, mDay)
    count = birth_count - die_count
    return count