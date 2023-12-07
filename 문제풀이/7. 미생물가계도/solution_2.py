global name_id, parent, m_parent, children, depth, A, B, sq, m


def sqrt_update(l, r):
    # print(l,r)
    while l <= r and l % sq:  # 블럭의 시작 부분이 아닐 때
        A[l] += 1
        l += 1
    while l <= r and (r + 1) % sq:  # 블럭의 끝 부분이 아닐 때
        A[r] += 1
        r -= 1
    while l <= r:
        B[l // sq] += 1
        l += sq


def lca_jump(a, b):
    dist = 0

    if depth[a] < depth[b]:
        a, b = b, a

    while depth[a] - m >= depth[b]:  # 이거 조건 제대로 기억!
        a = m_parent[a]
        dist += m

    while depth[a] != depth[b]:
        a = parent[a]
        dist += 1

    while m_parent[a] != m_parent[b]:
        a = m_parent[a]
        b = m_parent[b]
        dist += 2 * m

    while a != b:
        a = parent[a]
        b = parent[b]
        dist += 2

    return dist


def init(mAncestor: str, mDeathDay: int) -> None:
    global name_id, parent, m_parent, children, depth, A, B, sq, m

    name_id = {mAncestor: 0}

    parent = [0 for _ in range(12001)]  # 이렇게 나눠서 해야 더 안 헷갈리고 편함
    m_parent = [0 for _ in range(12001)]
    children = [[] for _ in range(12001)]
    depth = [0 for _ in range(12001)]

    A = [0 for _ in range(1000001)]
    B = [0 for _ in range(1001)]
    sq = 1000
    m = 45

    sqrt_update(0, mDeathDay)

    return


def add(mName: str, mParent: str, mBirthday: int, mDeathDay: int) -> int:
    name_id[mName] = len(name_id)  # 순차적으로 0,1,2 들어온 순으로 붙음
    child_id = name_id[mName]
    parent_id = name_id[mParent]

    parent[child_id] = parent_id
    depth[child_id] = depth[parent_id] + 1
    children[parent_id].append(child_id)

    m_parent_id = child_id
    for _ in range(m):
        if m_parent_id == 0: break
        m_parent_id = parent[m_parent_id]  # m번 부모 타기

    m_parent[child_id] = m_parent_id

    sqrt_update(mBirthday, mDeathDay)

    return depth[child_id]


def distance(mName1: str, mName2: str) -> int:
    # lca_m_jump 사용
    a = name_id[mName1]
    b = name_id[mName2]

    return lca_jump(a, b)


def count(mDay: int) -> int:
    return A[mDay] + B[mDay // sq]