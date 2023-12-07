from typing import List
from collections import defaultdict
import heapq

# 데이터 관리, 지우기 쉽게 하기 위해
db = dict()  # message_id: comment_id: [reply_id, ...]
cmt_to_message = dict()
reply_to_cmt = dict()

# lazy pq를 위한 정답지
user_points = defaultdict(int)  # mUser: total_point
message_point = dict()  # message_id: total_point
org_message_point = dict()  # message_id: point, erase를 위해 쓰일거임
comment_point = dict()  # comment_id: point
reply_point = dict()  # reply_id: point

mID_to_user = dict()  # mID: mUser 이 글을 쓴 유저가 누구인지! erase 할때 필요

# heap
user_max_heap = []  # (-point, mUser) # 포인트가 높고, 사전순으로 앞선, 사전 역순으로 문제가 나오면 어떻게 해야하지??
message_max_heap = []  # (-point, message_id) # 포인트가 높고, 작은 글 ID


def init() -> None:
    db.clear()
    cmt_to_message.clear()
    reply_to_cmt.clear()

    user_points.clear()
    message_point.clear()
    org_message_point.clear()
    comment_point.clear()
    reply_point.clear()

    mID_to_user.clear()

    user_max_heap.clear()
    message_max_heap.clear()


def writeMessage(mUser: str, mID: int, mPoint: int) -> int:
    mID_to_user[mID] = mUser

    user_points[mUser] += mPoint
    heapq.heappush(user_max_heap, (-user_points[mUser], mUser))

    if mID not in message_point:
        message_point[mID] = 0
    message_point[mID] += mPoint
    org_message_point[mID] = mPoint

    db[mID] = dict()
    heapq.heappush(message_max_heap, (-message_point[mID], mID))

    return user_points[mUser]


def commentTo(mUser: str, mID: int, mTargetID: int, mPoint: int) -> int:
    """ 글의 총합 포인트를 return 해야함, 진짜 헷갈리게 해놨네"""
    # 글쓴 사람 지정하고, user 점수 올리기
    mID_to_user[mID] = mUser
    user_points[mUser] += mPoint
    heapq.heappush(user_max_heap, (-user_points[mUser], mUser))

    # target 이 글이냐 댓글이냐
    messge_id = None
    if mTargetID in message_point:  # 글에 댓글을 달때
        messge_id = mTargetID
        comment_point[mID] = mPoint  # comment_id point 추가
        db[messge_id][mID] = list()  # reply 를 받을 수 있게 준비 함
        cmt_to_message[mID] = messge_id  # 역 추적을 위한

        # message_point 업데이트 및 heappush
        message_point[messge_id] += mPoint
        heapq.heappush(message_max_heap, (-message_point[messge_id], messge_id))


    elif mTargetID in comment_point:  # 댓글에 답글을 달때
        # 역으로 message_id 를 구해야함
        messge_id = cmt_to_message[mTargetID]
        db[messge_id][mTargetID].append(mID)
        reply_to_cmt[mID] = mTargetID  # 역 추적 용

        reply_point[mID] = mPoint

        # message_point 업데이트 및 heappush
        message_point[messge_id] += mPoint
        heapq.heappush(message_max_heap, (-message_point[messge_id], messge_id))

    return message_point[messge_id]


def push_user_pq(attacked_users: List[str]):
    # 다시 user heap 에 넣기
    for user in attacked_users:
        point = user_points[user]
        if point > 0:
            heapq.heappush(user_max_heap, (-point, user))


def erase(mID: int) -> int:
    """
    유저 점수도 내려야함, 그리고 다시 push 해야 한다
    다른 유저들도 피해 받는게 많은데? 제일 밑에꺼 부터 찬찬히 제거해 나가자
    -------

    """
    attacked_users = []
    if mID in message_point:
        # 정답지 완전 제거
        message_id = mID
        message_point.pop(message_id)

        messge_owner: str = mID_to_user.pop(message_id)
        _org_message_point: int = org_message_point.pop(message_id)
        user_points[messge_owner] -= _org_message_point

        attacked_users.append(messge_owner)

        for cmt_id, reply_ids in db[message_id].items():
            mUser = mID_to_user.pop(cmt_id)
            _cpoint: int = comment_point.pop(cmt_id)
            attacked_users.append(mUser)
            user_points[mUser] -= _cpoint
            cmt_to_message.pop(cmt_id)

            for reply_id in reply_ids:
                reply_to_cmt.pop(reply_id)
                mUser = mID_to_user.pop(reply_id)
                _rpoint: int = reply_point.pop(reply_id)
                attacked_users.append(mUser)

                user_points[mUser] -= _rpoint

        db.pop(message_id)  # 구조 만들어 둔거 제거
        # user heapq
        push_user_pq(attacked_users)

        return user_points[messge_owner]


    elif mID in comment_point:
        cmt_id = mID
        comment_user = mID_to_user.pop(cmt_id)
        _cpoint = comment_point.pop(cmt_id)

        user_points[comment_user] -= _cpoint
        attacked_users.append(comment_user)
        message_id = cmt_to_message.pop(cmt_id)
        # commet 제거
        message_point[message_id] -= _cpoint

        for reply_id in db[message_id][cmt_id]:
            reply_to_cmt.pop(reply_id)
            mUser = mID_to_user.pop(reply_id)
            _rpoint: int = reply_point.pop(reply_id)
            attacked_users.append(mUser)

            user_points[mUser] -= _rpoint
            message_point[message_id] -= _rpoint

        db[message_id].pop(cmt_id)
        push_user_pq(attacked_users)
        heapq.heappush(message_max_heap, (-message_point[message_id], message_id))
        return message_point[message_id]

    elif mID in reply_point:
        reply_user = mID_to_user.pop(mID)
        attacked_users.append(reply_user)
        _rpoint = reply_point.pop(mID)
        user_points[reply_user] -= _rpoint

        # message 정답지 업데이트
        cmt_id = reply_to_cmt[mID]
        messge_id = cmt_to_message[cmt_id]
        db[messge_id][cmt_id].remove(mID)  # 제거

        message_point[messge_id] -= _rpoint

        push_user_pq(attacked_users)
        heapq.heappush(message_max_heap, (-message_point[messge_id], messge_id))
        return message_point[messge_id]


def getBestMessages(mBestMessageList: List[int]) -> None:
    tmp = set()
    # 중복 처리가 필요함
    while message_max_heap:
        point, message_id = map(abs, heapq.heappop(message_max_heap))  # (-point, message_id)

        # 정답과 같지 않을때 넘기기
        if message_id not in message_point:
            continue
        if point != message_point[message_id]:
            continue
        tmp.add((point, message_id))
        # 5개 넣었으면 그만
        if len(tmp) == 5:
            break

    # 다시 넣기
    for idx, (point, message_id) in enumerate(tmp):
        heapq.heappush(message_max_heap, (-point, message_id))
        mBestMessageList[idx] = message_id


def getBestUsers(mBestUserList: List[str]) -> None:
    tmp = set()
    while user_max_heap:
        point, mUser = heapq.heappop(user_max_heap)  # (-point, mUser)
        point = abs(point)

        # 정답과 같지 않을때 넘기기
        if point != user_points[mUser]:
            continue

        tmp.add((point, mUser))
        # 5개 넣었으면 그만
        if len(tmp) == 5:
            break

    # 다시 넣기
    for idx, (point, mUser) in enumerate(tmp):
        heapq.heappush(user_max_heap, (-point, mUser))
        mBestUserList[idx] = mUser