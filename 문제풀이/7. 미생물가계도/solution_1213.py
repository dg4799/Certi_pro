"""
선조 Ancestor를 받아서 개체간의 거리를 반환하면 된다.
bisect를 활용해서 Firstdaty, Lastday를 체크하면됌

LCA를 돌리면 되는데...
1. depth가 깊은쪽을 체크해서 자리를 바꾼다
2. while로 depth가 같아질때까지 돌린다
  - depth가 같지않으면 depth가 깊은쪽의 부모값을 인덱스로 저장  index = parent(index), res += 1
3. while로 depth가 같으면
  - 두 덱스의 parent가 같은지 체크
  - 각각 인덱스를 parent(index)로 바꾸고 res += 1씩


-init
1. depth 리스트
2. parent 리스트
4. idx = 0
3. Name_list = {}
4. Name_list[조상] = idx
5. birth_list = []
6. die_list = []

- add
1. idx += 1
2. "이름" : idx로 리스트 저장
3. parent 리스트에 저장 : parent[idx] = parent[Name_list[mParent]]
4. depth에 저장 : depth[idx] = depth[Name_list[mParent]] + 1
5. birth_list에 저장 : insort_right
6. die_list도 똑같이 저장

- distance
1. depth가 깊은쪽을 체크해서 자리를 바꾼다
2. while로 depth가 같아질때까지 돌린다
  - depth가 같지않으면 depth가 깊은쪽의 부모값을 인덱스로 저장  index = parent(index), res += 1
3. while로 depth가 같으면
  - 두 덱스의 parent가 같은지 체크
  - 각각 인덱스를 parent(index)로 바꾸고 res += 1씩

- count
1. birth_list를 bisect로 체크
2. die_list를 bisect_left로 체크

== Day 900
 1. birth bisect = 6
 2. die bisect bisect = 2
   = bisect 6-2 = 4

== Day 800
 1. birth bisect = 6
 2. die bisect = 1
   = bisect 6-1 = 5

== Day 700
 1. birth bisect = 5
 2. die bisect = 0
   = bisect 5-0 = 5

== Day 300
 1. birth bisect = 3
 2. die bisect = 0
   = bisect 3-0 = 3




"""

from bisect import insort, bisect_left, bisect_right
def init(mAncestor:str, mDeathDay:int) -> None:
    """
    -init
1. depth 리스트
2. parent 리스트
4. idx = 0
3. Name_list = {}
4. Name_list[조상] = idx
5. birth_list = []
6. die_list = []
    """
    global depth, parent, idx, Name_list, birth_list, die_list

    depth = [0]
    parent = [0]
    idx = 0
    Name_list = {}
    Name_list[mAncestor] = idx
    birth_list = [0]
    die_list = [mDeathDay]

def add(mName:str, mParent:str, mBirthday:int, mDeathDay:int)-> int:
    global depth, parent, idx, Name_list, birth_list, die_list

    """
    1. idx += 1
    2. "이름" : idx로 리스트 저장
    3. parent 리스트에 저장 : parent[idx] = parent[Name_list[mParent]]
    4. depth에 저장 : depth[idx] = depth[Name_list[mParent]] + 1
    5. birth_list에 저장 : insort_right
    6. die_list도 똑같이 저장
    """
    idx += 1
    Name_list[mName] = idx
    parent.append(Name_list[mParent])
    depth.append(depth[Name_list[mParent]] + 1)
    insort(birth_list, mBirthday)
    insort(die_list, mDeathDay)
    return depth[idx]

def distance(mName1:str, mName2:str)-> int:
    """
    1. depth가 깊은쪽을 체크해서 자리를 바꾼다
    2. while로 depth가 같아질때까지 돌린다
      - depth가 같지않으면 depth가 깊은쪽의 부모값을 인덱스로 저장  index = parent(index), res += 1
    3. while로 depth가 같으면
      - 두 덱스의 parent가 같은지 체크
      - 각각 인덱스를 parent(index)로 바꾸고 res += 1씩
    """
    global depth, parent, idx, Name_list, birth_list, die_list


    index_1, index_2 = Name_list[mName1], Name_list[mName2]

    if depth[index_1] > depth[index_2]:
        index_1, index_2 = index_2, index_1

    res = 0
    while depth[index_1] != depth[index_2]:
        index_2 = parent[index_2]
        res += 1
    while index_1 != index_2:
        index_1 = parent[index_1]
        index_2 = parent[index_2]
        res += 2

    return res

def count(mDay:int) -> int:

    """
    - count
1. birth_list를 bisect로 체크
2. die_list를 bisect_left로 체크
    """
    global depth, parent, idx, Name_list, birth_list, die_list

    birth_check = bisect_right(birth_list, mDay)
    die_check = bisect_left(die_list, mDay)

    return birth_check - die_check