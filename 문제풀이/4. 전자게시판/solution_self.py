import heapq
from typing import List
from collections import defaultdict

def init() -> None:
    global Message, Comment, Recomment, User_point, best_Message, best_User
    Message = {}
    Comment = {}
    Recomment = {}
    User_point = defaultdict(int)
    best_Message = []
    best_User = []
    pass


def writeMessage(mUser: str, mID: int, mPoint: int) -> int:
    User_point[mUser] += mPoint
    heapq.heappush(best_User, (-User_point[mUser], mUser))
    Message[mID] = [mUser, mPoint, mPoint, []]
    heapq.heappush(best_Message, (-mPoint, mID))
    return User_point[mUser]


def commentTo(mUser: str, mID: int, mTargetID: int, mPoint: int) -> int:
    User_point[mUser] += mPoint
    heapq.heappush(best_User, (-User_point[mUser], mUser))

    if mTargetID in Message:
        Message[mTargetID][1] += mPoint
        Message[mTargetID][3].append(mID)
        Comment[mID] = [mUser, mPoint, [mTargetID], []]
        heapq.heappush(best_Message, (-Message[mTargetID][1], mTargetID))
        return Message[mTargetID][1]

    elif mTargetID in Comment:
        Message_id = Comment[mTargetID][2][0]
        Message[Message_id][1] += mPoint
        Comment[mTargetID][3].append(mID)
        Recomment[mID] = [mUser, mPoint, [mTargetID]]
        heapq.heappush(best_Message, (-Message[Message_id][1], Message_id))
        return Message[Message_id][1]



def erase(mID: int) -> int:
    if mID in Message:
        User_point[Message[mID][0]] -= Message[mID][2]
        heapq.heappush(best_User, (-User_point[Message[mID][0]], Message[mID][0]))
        Message[mID][1] = 0
        heapq.heappush(best_Message, (-Message[mID][1], mID))
        for comment_id in Message[mID][3]:
            User_point[Comment[comment_id][0]] -= Comment[comment_id][1]
            heapq.heappush(best_User, (-User_point[Comment[comment_id][0]], Comment[comment_id][0]))
            for recomment_id in Comment[comment_id][3]:
                User_point[Recomment[recomment_id][0]] -= Recomment[recomment_id][1]
                heapq.heappush(best_User, (-User_point[Recomment[recomment_id][0]], Recomment[recomment_id][0]))
        return User_point[Message[mID][0]]
    elif mID in Comment:
        User_point[Comment[mID][0]] -= Comment[mID][1]
        heapq.heappush(best_User, (-User_point[Comment[mID][0]], Comment[mID][0]))
        Message_id = Comment[mID][2][0]
        Message[Message_id][1] -= Comment[mID][1]
        for recomment_id in Comment[mID][3]:
            User_point[Recomment[recomment_id][0]] -= Recomment[recomment_id][1]
            heapq.heappush(best_User, (-User_point[Recomment[recomment_id][0]], Recomment[recomment_id][0]))
            Message_id = Comment[mID][2][0]
            Message[Message_id][1] -= Recomment[recomment_id][1]
            heapq.heappush(best_Message, (-Message[Message_id][1], Message_id))
        Message_id = Comment[mID][2][0]

        Message[Message_id][3].remove(mID)
        heapq.heappush(best_Message, (-Message[Comment[mID][2][0]][1], Message_id))

        return Message[Message_id][1]
    elif mID in Recomment:
        User_point[Recomment[mID][0]] -= Recomment[mID][1]
        heapq.heappush(best_User, (-User_point[Recomment[mID][0]], Recomment[mID][0]))
        comment_id = Recomment[mID][2][0]
        Message_id = Comment[comment_id][2][0]
        Message[Message_id][1] -= Recomment[mID][1]
        Comment[comment_id][3].remove(mID)
        heapq.heappush(best_Message, (-Message[Message_id][1], Message_id))

    return Message[Message_id][1]


def getBestMessages(mBestMessageList: List[int]) -> None:
    temps = []
    while len(temps) != 5:
        temp = heapq.heappop(best_Message)
        score, Message_id = -temp[0], temp[1]
        if score != Message[Message_id][1] or temp in temps:
            continue
        temps.append(temp)
    i = 1
    for score, Message_id in temps:
        heapq.heappush(best_Message, (score, Message_id))
        mBestMessageList[i-1] = Message_id
        i += 1



def getBestUsers(mBestUserList: List[str]) -> None:
    global Message, Comment, Recomment, User_point, best_Message, best_User

    temps = []
    while len(temps) != 5:
        temp = heapq.heappop(best_User)
        score, User_name = -temp[0], temp[1]
        if score != User_point[User_name] or temp in temps:
            continue
        temps.append(temp)
    i = 1
    for score, User_name in temps:
        heapq.heappush(best_User, (score, User_name))
        mBestUserList[i-1] = User_name
        i += 1

