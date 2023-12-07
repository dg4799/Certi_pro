from typing import List
from collections import defaultdict
import heapq

bestMessages = []  # (-글 점수, 글ID)의 힙

bestUsers = []  # (-유저 점수, 유저이름)의 힙
# 유저가 완전 삭제되지는 않음

userNameToScore = defaultdict(int)

userScore = defaultdict(int)
messageScore = defaultdict(int)
messagePureScore = defaultdict(int)  # 댓글, 답글 제외한 점수
commentScore = defaultdict(int)
commentPureScore = defaultdict(int)  # 답글 제외한 점수
replyScore = defaultdict(int)

messageNo = set()
commentNo = set()
replyNo = set()

messageWrite = dict()
commentWrite = dict()
replyWrite = dict()
commentParent = dict()
replyParent = dict()
messageChild = dict()  # 글 삭제 시 댓글, 답글 모두 삭제 및 점수 회수, 댓글 삭제 시 답글에 대하여 마찬가지
commentChild = dict()


def init() -> None:
    global bestMessages
    global bestUsers
    global userNameToScore
    global userScore, messageScore, messagePureScore, commentScore, commentPureScore, replyScore
    global messageNo, commentNo, replyNo
    global messageWrite, commentWrite, replyWrite, commentParent, replyParent, messageChild, commentChild
    bestMessages = []  # (-글 점수, 글ID)의 힙

    bestUsers = []  # (-유저 점수, 유저이름)의 힙
    # 유저가 완전 삭제되지는 않음

    userNameToScore = defaultdict(int)

    userScore = defaultdict(int)
    messageScore = defaultdict(int)
    messagePureScore = defaultdict(int)  # 댓글, 답글 제외한 점수
    commentScore = defaultdict(int)
    commentPureScore = defaultdict(int)  # 답글 제외한 점수
    replyScore = defaultdict(int)

    messageNo = set()
    commentNo = set()
    replyNo = set()

    messageWrite = dict()
    commentWrite = dict()
    replyWrite = dict()
    commentParent = dict()
    replyParent = dict()
    messageChild = dict()  # 글 삭제 시 댓글, 답글 모두 삭제 및 점수 회수, 댓글 삭제 시 답글에 대하여 마찬가지
    commentChild = dict()


def writeMessage(mUser: str, mID: int, mPoint: int) -> int:
    messageNo.add(mID)

    userScore[mUser] += mPoint
    heapq.heappush(bestUsers, (-userScore[mUser], mUser))
    messageWrite[mID] = mUser

    messagePureScore[mID] = mPoint
    messageScore[mID] += mPoint
    heapq.heappush(bestMessages, (-mPoint, mID))

    return userScore[mUser]


def commentTo(mUser: str, mID: int, mTargetID: int, mPoint: int) -> int:
    result = -1
    if mTargetID in messageNo:  # 댓글 작성
        commentNo.add(mID)
        commentWrite[mID] = mUser

        commentScore[mID] = mPoint  # 댓글 점수 반영
        commentPureScore[mID] = mPoint
        userScore[mUser] += mPoint
        heapq.heappush(bestUsers, (-userScore[mUser], mUser))

        messageScore[mTargetID] += mPoint  # 댓글의 글에 대해 점수 반영
        heapq.heappush(bestMessages, (-messageScore[mTargetID], mTargetID))
        commentParent[mID] = mTargetID
        if mTargetID not in messageChild:
            messageChild[mTargetID] = set()
        messageChild[mTargetID].add(mID)

        result = messageScore[mTargetID]  # 글의 점수 리턴
    elif mTargetID in commentNo:  # 답글 작성
        replyNo.add(mID)
        replyWrite[mID] = mUser

        replyScore[mID] = mPoint  # 답글 점수 반영
        userScore[mUser] += mPoint
        heapq.heappush(bestUsers, (-userScore[mUser], mUser))

        commentScore[mTargetID] += mPoint  # 답글의 댓글에 대해 점수 반영
        replyParent[mID] = mTargetID
        if mTargetID not in commentChild:
            commentChild[mTargetID] = set()
        commentChild[mTargetID].add(mID)

        messageScore[commentParent[mTargetID]] += mPoint  # 답글의 댓글의 글에 대해 점수 반영
        heapq.heappush(bestMessages, (-messageScore[commentParent[mTargetID]], commentParent[mTargetID]))

        result = messageScore[commentParent[mTargetID]]  # 글의 점수 리턴

    return result


def erase(mID: int) -> int:
    result = 0
    if mID in messageNo:
        # 글에 대한 댓글, 답글 삭제 처리는 안해도 됨. commentTo 호출 전제조건 때문
        if mID in messageChild:
            for e in list(messageChild[mID]):
                erase(e)

        userScore[messageWrite[mID]] -= messagePureScore[mID]
        heapq.heappush(bestUsers, (-userScore[messageWrite[mID]], messageWrite[mID]))

        messageScore[mID] = 0
        result = userScore[messageWrite[mID]]
    elif mID in commentNo:
        if mID in commentChild:
            for e in list(commentChild[mID]):
                erase(e)

        mIDMessage = commentParent[mID]

        messageScore[mIDMessage] -= commentPureScore[mID]
        heapq.heappush(bestMessages, (-messageScore[mIDMessage], mIDMessage))

        userScore[commentWrite[mID]] -= commentPureScore[mID]
        heapq.heappush(bestUsers, (-userScore[commentWrite[mID]], commentWrite[mID]))

        messageChild[mIDMessage].discard(mID)

        result = messageScore[mIDMessage]
    elif mID in replyNo:
        mIDComment = replyParent[mID]
        mIDMessage = commentParent[mIDComment]

        commentScore[mIDComment] -= replyScore[mID]

        messageScore[mIDMessage] -= replyScore[mID]
        heapq.heappush(bestMessages, (-messageScore[mIDMessage], mIDMessage))

        userScore[replyWrite[mID]] -= replyScore[mID]
        heapq.heappush(bestUsers, (-userScore[replyWrite[mID]], replyWrite[mID]))

        result = messageScore[mIDMessage]

        commentChild[mIDComment].discard(mID)

    return result


def getBestMessages(mBestMessageList: List[int]) -> None:
    result = []
    backup = []

    while len(result) < 5:
        while -bestMessages[0][0] > messageScore[bestMessages[0][1]]:
            heapq.heappop(bestMessages)
        temp = heapq.heappop(bestMessages)
        if temp[1] in result:
            continue
        result.append(temp[1])
        backup.append(temp)
    for e in backup:
        heapq.heappush(bestMessages, e)  # 5개 뽑았던 것 다시 집어넣음

    for i in range(len(mBestMessageList)):
        mBestMessageList[i] = result[i]


def getBestUsers(mBestUserList: List[str]) -> None:
    result = []
    backup = []

    while len(result) < 5:
        while -bestUsers[0][0] > userScore[bestUsers[0][1]]:
            heapq.heappop(bestUsers)
        temp = heapq.heappop(bestUsers)
        if temp[1] in result:
            continue
        result.append(temp[1])
        backup.append(temp)
    for e in backup:
        heapq.heappush(bestUsers, e)  # 5개 뽑았던 것 다시 집어넣음

    for i in range(len(mBestUserList)):
        mBestUserList[i] = result[i]