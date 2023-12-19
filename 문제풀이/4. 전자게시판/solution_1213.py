"""
글, 댓글, 대댓글이 작성됨
글이 삭제될 때는 댓글과 답글이 모두 삭제
글, 댓글, 대댓글은 각각 포인트를 가짐
포인트들을 이용하여 베스트글 또는 베스트 유저를 찾아 보여준다(내림차순 5명 --> heap으로 5개만 골라내기)
 - ID별 포인트 기록, 글별 포인트 기록

- writeMessage
1. mUser인 사용자가 mPoint인 글을 작성하고 게시판에 등록
  - 글 리스트에 mID, mUser,mPoint(글 자체 포인트), mPoint(글의 합계 포인트), 자식리스트 []로 list에 추가
  - 유저리스트에 point를 add
  - 베스트 유저 리스트에 유저와 point를 add
  - 베스트 글 리스트에 글 총합 mPoint와 mID를 add

- commentTo
1. mTargetID가 글이면
  - 댓글 mID를 달고 글 mTargetID의 총합 포인트를 반환
    1. 댓글 리스트에 mID, mUser,mPoint(글 자체 포인트), 부모mID, 자식리스트 []로 list에 추가
    2. mTargetID를 글 리스트에서 찾아서 mPoint에 포인트 추가, 자식리스트에 mID append
    3. 유저리스트에 point add
    4. 베스트 유저 리스트에 유저와 point add
    5. 베스트 글 리스트에 글 총합 mPoint와 mID를 add
    6. 글의 총합 포인트를 반환
2. mTargerID가 댓글이면
  - 대댓글 mID를 달고 댓글 mTargetID가 달린 글의 총합 포인트를 반환한다
    1. 대댓글 리스트에 mID, 댓글 mID, mUser, mPoint로 list에 추가
    2. mTargetID를 댓글 리스트에 찾아서 자식 리스트에 mID append
    3. 댓글리스트를 글리스트에서 찾아서 mPoint에 포인트 추가
    4. 유저리스트에 point add
    5. 베스트 글 리스트에 글 총합 mPoint와 mID를 add
    6. 글의 총합 포인트를 반환

- erase
1. mID가 글인 경우 mID를 작성한 사용자의 총합 포인트를 반환
  - 글인 경우
    - 글의 mUser의 point를 깎는다 -> 베스트 유저에 추가
    - 글의 댓글에 들어가서 mUser point를 깎는다 - 베스트 유저에 추가
    - 댓글의 대댓글에 들어가서 mUser Point를 깎는다 -> 베스트 유저에 추가
    - 글 삭제
2. mID가 댓글 또는 대댓글인경우 삭제된 댓글 또는 대댓글이 달려있었던 글의 총합 포인트를 반환
  - 댓글인경우
    - 댓글의 글을 찾아서 mPoint를 차감시킨다
    - 글의 자식리스트에서 댓글 mID를 지운다
    - 댓글의 mUser Point를 깎는다 -> 베스트 유저에 추가
    - 댓글의 대댓글에 들어가서 똑같이 반복한다
      - 글을 찾아서 mPoint 차감
      - mUser Point를 깎는다 -> 베스트 유저에 추가
    - 베스트글 리스트에 글을 추가한다

- getBestMessages
  1. 총합포인트가 가장 높은 5개의 ID를 내림차순으로 mBestMessageList에 저장, 총합포인트가 같은 경우 mID가 더 작은글의 ID가 먼저온다. (heap으로 point, mID)
   - Temp 리스트를 만든다
   - while로 heap에서 pop을 해온다 -> point, mID
   - point, mid가 글리스트에 없거나 Temp 리스트에 이미 있으면 continue
   - Temp리스트에 point, mID를 heap 추가한다
   - for 문으로 5번 반복
     - 다시 Temp리스트를 pop으로 뽑는다
     - mBestMessage에 값을 넣는다
     - 값을 글 리스트에 push 한다 (최신화)

- getBestUser
  1. getBestMessage와 동일함.
"""




from typing import List
from collections import defaultdict
from heapq import heappop, heappush

def init() -> None:
    """
    글, 댓글, 대댓글이 작성됨
글이 삭제될 때는 댓글과 답글이 모두 삭제
글, 댓글, 대댓글은 각각 포인트를 가짐
포인트들을 이용하여 베스트글 또는 베스트 유저를 찾아 보여준다(내림차순 5명 --> heap으로 5개만 골라내기)
 - ID별 포인트 기록, 글별 포인트 기록
    """
    global Message, comment, recomment, bestUser, bestMessage, user_list
    Message = {}
    comment = {}
    recomment = {}
    user_list = defaultdict(int)
    bestUser = []
    bestMessage = []
    pass


def writeMessage(mUser: str, mID: int, mPoint: int) -> int:
    """
    1. mUser인 사용자가 mPoint인 글을 작성하고 게시판에 등록
  - 글 리스트에 mID, mUser,mPoint(글 자체 포인트), mPoint(글의 합계 포인트), 자식리스트 []로 list에 추가
  - 유저리스트에 point를 add
  - 베스트 유저 리스트에 유저와 point를 add
  - 베스트 글 리스트에 글 총합 mPoint와 mID를 add
    """
    global Message, comment, recomment, bestUser, bestMessage, user_list

    Message[mID] = [mUser, mPoint, mPoint, []]
    user_list[mUser] += mPoint
    heappush(bestUser, (-user_list[mUser], mUser))
    heappush(bestMessage, (-mPoint, mID))

    return user_list[mUser]


def commentTo(mUser: str, mID: int, mTargetID: int, mPoint: int) -> int:
    global Message, comment, recomment, bestUser, bestMessage, user_list

    user_list[mUser] += mPoint
    heappush(bestUser, (-user_list[mUser], mUser))

    if mTargetID in Message:
        """
    1. mTargetID가 글이면
      - 댓글 mID를 달고 글 mTargetID의 총합 포인트를 반환
        1. 댓글 리스트에 mID, mUser,mPoint(글 자체 포인트), 부모mID, 자식리스트 []로 list에 추가
        2. mTargetID를 글 리스트에서 찾아서 mPoint에 포인트 추가, 자식리스트에 mID append
        3. 유저리스트에 point add
        4. 베스트 유저 리스트에 유저와 point add
        5. 베스트 글 리스트에 글 총합 mPoint와 mID를 add
        6. 글의 총합 포인트를 반환
        """
        Message[mTargetID][2] += mPoint
        Message[mTargetID][3].append(mID)
        comment[mID] = [mUser, mPoint, mTargetID, []]
        heappush(bestMessage, (-Message[mTargetID][2], mTargetID))
        return Message[mTargetID][2]

    elif mTargetID in comment:
        """
    2. mTargerID가 댓글이면
      - 대댓글 mID를 달고 댓글 mTargetID가 달린 글의 총합 포인트를 반환한다
        1. 대댓글 리스트에 mID, 댓글 mID, mUser, mPoint로 list에 추가
        2. mTargetID를 댓글 리스트에 찾아서 자식 리스트에 mID append
        3. 댓글리스트를 글리스트에서 찾아서 mPoint에 포인트 추가
        4. 유저리스트에 point add
        5. 베스트 글 리스트에 글 총합 mPoint와 mID를 add
        6. 글의 총합 포인트를 반환
        """
        Message[comment[mTargetID][2]][2] += mPoint

        comment[mTargetID][3].append(mID)
        recomment[mID] = [mUser, mPoint, mTargetID]
        heappush(bestMessage, (-Message[comment[mTargetID][2]][2], comment[mTargetID][2]))
    return Message[comment[mTargetID][2]][2]


def erase(mID: int) -> int:
    """
    - erase

    """
    global Message, comment, recomment, bestUser, bestMessage, user_list

    if mID in Message:
        """
        - 글인 경우
         - 글의 mUser의 point를 깎는다 -> 베스트 유저에 추가
         - 글의 댓글에 들어가서 mUser point를 깎는다 - 베스트 유저에 추가
         - 댓글의 대댓글에 들어가서 mUser Point를 깎는다 -> 베스트 유저에 추가
         - 글 삭제
        """
        user_list[Message[mID][0]] -= Message[mID][1]
        heappush(bestUser, (-user_list[Message[mID][0]], Message[mID][0]))

        Message[mID][2] = 0
        heappush(bestMessage, (-Message[mID][2], mID))

        for comment_id in Message[mID][3]:
            user_list[comment[comment_id][0]] -= comment[comment_id][1]
            heappush(bestUser, (-user_list[comment[comment_id][0]], comment[comment_id][0]))
            for recomment_id in comment[comment_id][3]:
                user_list[recomment[recomment_id][0]] -= recomment[recomment_id][1]
                heappush(bestUser, (-user_list[recomment[recomment_id][0]], recomment[recomment_id][0]))
        return user_list[Message[mID][0]]

    elif mID in comment:
        """
        - 댓글인경우
            - 댓글의 글을 찾아서 mPoint를 차감시킨다
            - 글의 자식리스트에서 댓글 mID를 지운다
            - 댓글의 mUser Point를 깎는다 -> 베스트 유저에 추가
         - 댓글의 대댓글에 들어가서 똑같이 반복한다
              - 글을 찾아서 mPoint 차감
              - mUser Point를 깎는다 -> 베스트 유저에 추가
              - 베스트글 리스트에 글을 추가한다
        """
        user_list[comment[mID][0]] -= comment[mID][1]
        heappush(bestUser, (-user_list[comment[mID][0]], comment[mID][0]))
        Message[comment[mID][2]][2] -= comment[mID][1]
        for recomment_id in comment[mID][3]:
            user_list[recomment[recomment_id][0]] -= recomment[recomment_id][1]
            heappush(bestUser, (-user_list[recomment[recomment_id][0]], recomment[recomment_id][0]))
            p_comment = recomment[recomment_id][2]
            Message[comment[p_comment][2]][2] -= recomment[recomment_id][1]
            heappush(bestMessage, (-Message[comment[p_comment][2]][2], comment[p_comment][2]))


        Message[comment[mID][2]][3].remove(mID)
        heappush(bestMessage, (-Message[comment[mID][2]][2], comment[mID][2]))
        return Message[comment[mID][2]][2]


    elif mID in recomment:
        user_list[recomment[mID][0]] -= recomment[mID][1]
        heappush(bestUser, (-user_list[recomment[mID][0]], recomment[mID][0]))
        p_comment = recomment[mID][2]
        Message[comment[p_comment][2]][2] -= recomment[mID][1]
        comment[p_comment][3].remove(mID)
        heappush(bestMessage, (-Message[comment[p_comment][2]][2], comment[p_comment][2]))
        return Message[comment[p_comment][2]][2]


def getBestMessages(mBestMessageList: List[int]) -> None:
    """
    - getBestMessages
      1. 총합포인트가 가장 높은 5개의 ID를 내림차순으로 mBestMessageList에 저장, 총합포인트가 같은 경우 mID가 더 작은글의 ID가 먼저온다. (heap으로 point, mID)
       - Temp 리스트를 만든다
       - while로 heap에서 pop을 해온다 -> point, mID
       - point, mid가 글리스트에 없거나 Temp 리스트에 이미 있으면 continue
       - Temp리스트에 point, mID를 heap 추가한다
       - for 문으로 5번 반복
         - 다시 Temp리스트를 pop으로 뽑는다
         - mBestMessage에 값을 넣는다
         - 값을 글 리스트에 push 한다 (최신화)

    - getBestUser
      1. getBestMessage와 동일함.
    """
    global Message, comment, recomment, bestUser, bestMessage, user_list




    temps = []

    while len(temps) != 5:
        try:
            temp = heappop(bestMessage)
            Point, mID = -temp[0], temp[1]
            if Message[mID][2] != Point or temp in temps: continue
            temps.append(temp)
        except:
            pass

    i = 1
    for Point, mID in temps:
        heappush(bestMessage, (Point, mID))
        mBestMessageList[i-1] = mID
        i += 1


def getBestUsers(mBestUserList: List[str]) -> None:
    """
    - getBestMessages
      1. 총합포인트가 가장 높은 5개의 ID를 내림차순으로 mBestMessageList에 저장, 총합포인트가 같은 경우 mID가 더 작은글의 ID가 먼저온다. (heap으로 point, mID)
       - Temp 리스트를 만든다
       - while로 heap에서 pop을 해온다 -> point, mID
       - point, mid가 글리스트에 없거나 Temp 리스트에 이미 있으면 continue
       - Temp리스트에 point, mID를 heap 추가한다
       - for 문으로 5번 반복
         - 다시 Temp리스트를 pop으로 뽑는다
         - mBestMessage에 값을 넣는다
         - 값을 글 리스트에 push 한다 (최신화)

    - getBestUser
      1. getBestMessage와 동일함.
    """
    global Message, comment, recomment, bestUser, bestMessage, user_list


    temps = []
    while len(temps) != 5:
        temp = heappop(bestUser)
        Point, User = -temp[0], temp[1]
        if user_list[User] != Point or temp in temps:
            continue
        temps.append(temp)

    i = 1
    for Point, User in temps:
        heappush(bestUser, (Point, User))
        mBestUserList[i-1] = User
        i += 1

"""
(★오답) list[mID]에 값을 넣을때 [mUser, mID, ....] 형태로 값을 넣어야 나중에 인덱스에 접근해서 값을 += 할 수 있음!!
(★오답) bestUser와 bestMessage에 값을 넣을때부터 -를 넣어서 자동정렬 가능하게 할 것!
(★오답) comment에서 recomment가 삭제되는 경우가 있는데 remove를 안해줘서 일부 케이스에서 실패함!
"""