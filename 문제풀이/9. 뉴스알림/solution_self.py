"""
- 타임라인으로 결과가 나와야 하기 때문에 타임라인을 업데이트하는 함수 필요
  1. 타임라인 업데이트 함수는 registerUser와 checkUser에서 먼저 알림을 보내는 경우가 있어 이때 실행하면 됨
  2. 업데이트 함수는 offerNews에서 뉴스를 받아서 업데이트 함수에서 해당 타임라인때 뉴스 알림을 주면됨
  3. 업데이트 리스트는 mTime을 heap뽑아서 처리함.
    - 입력받은 mTime이하의 업데이트 리스트들을 하나씩 꺼내서 처리한다.
    - 꺼낸 리스트에서 취소뉴스 리스트에 포함되어 있으면 continue
    - 아니면 유저리스트에 해당 뉴스를 추가함.

- registerUser
  1. 뉴스채널별 유저리스트를 저장함
  2. 뉴스채널에 유저가 없으면 리스트형태로 유저를 저장
  3. 뉴스채널에 유저가 있으면 리스트에 append하여 유저를 저장

- offerNews
  1. 입력받은 뉴스 정보를 업데이트 함수에서 처리하기 위해 업데이트 리스트에 heap으로 추가
   - mTime+mDelay -> heap의 시간
  * len(mChannelID) return

- cancleNews
  1. 뉴스ID가 중복이 아니기 때문에 취소뉴스 리스트에 모두 집어넣고 다른 함수에서 체크하면됨.

- checkuser
  1. update(time) 실행
  2. 유저가 받은 뉴스를 꺼내서 mRetIDs에 저장하고 뉴스 알림 갯수를 count해서 return
    - 취소뉴스 리스트에 포함되면 continue

"""
from collections import defaultdict
from heapq import heappop, heappush

def init(N:int, K:int) -> None:
    global CancleNews_list, User_news, update_list, NewsChannel
    """
    1. 취소뉴스 리스트 (중복없음)
    2. 유저가 받은 뉴스 리스트
    3. 업데이트 리스트
    4. 채널에 유저를 등록하기 위한 리스트
    """
    CancleNews_list = set()
    User_news = defaultdict(list)
    update_list = []
    NewsChannel = defaultdict(list)
    return

def registerUser(mTime:int, mUID:int, mNum:int, mChannelIDs:list) -> None:
    """
    - registerUser
  1. 뉴스채널별 유저리스트를 저장함
  2. 뉴스채널에 채널이 없으면 리스트형태로 유저를 저장
  3. 뉴스채널에 채널이 있으면 리스트에 append하여 유저를 저장
    """
    update(mTime)

    for i in range(mNum):
        if not mChannelIDs[i] in NewsChannel:
            NewsChannel[mChannelIDs[i]] = [mUID]
        else:
            NewsChannel[mChannelIDs[i]].append(mUID)
    return

def update(mTime):
    """
    - 타임라인으로 결과가 나와야 하기 때문에 타임라인을 업데이트하는 함수 필요
  1. 타임라인 업데이트 함수는 registerUser와 checkUser에서 먼저 알림을 보내는 경우가 있어 이때 실행하면 됨
  2. 업데이트 함수는 offerNews에서 뉴스를 받아서 업데이트 함수에서 해당 타임라인때 뉴스 알림을 주면됨
  3. 업데이트 리스트는 mTime을 heap뽑아서 처리함.
    - 입력받은 mTime이하의 업데이트 리스트들을 하나씩 꺼내서 처리한다.
    - 꺼낸 리스트에서 취소뉴스 리스트에 포함되어 있으면 continue
    - 아니면 유저리스트에 해당 뉴스를 추가함.
    """
    while len(update_list) != 0 and update_list[0][0] <= mTime:
        Time, mNewsID, mChannelID = heappop(update_list)
        if mNewsID in CancleNews_list: continue
        for User in NewsChannel[mChannelID]:
            User_news[User].append(mNewsID)

def offerNews(mTime:int, mNewsID:int, mDelay:int, mChannelID:int) -> int:
    """
    - offerNews
  1. 입력받은 뉴스 정보를 업데이트 함수에서 처리하기 위해 업데이트 리스트에 heap으로 추가
   - mTime+mDelay -> heap의 시간
  * len(mChannelID) return
    """
    heappush(update_list, (mTime+mDelay, mNewsID, mChannelID))
    return len(NewsChannel[mChannelID])

def cancelNews(mTime:int, mNewsID:int) -> None:
    CancleNews_list.add(mNewsID)
    return

def checkUser(mTime:int, mUID:int, mRetIDs:list)-> int:
    """
    - checkuser
  1. update(time) 실행
  2. 유저가 받은 뉴스를 꺼내서 mRetIDs에 저장하고 뉴스 알림 갯수를 count해서 return
    - 취소뉴스 리스트에 포함되면 continue
    """
    update(mTime)

    count = 0
    while len(User_news[mUID]) != 0:
        News = User_news[mUID].pop(-1)
        if News in CancleNews_list: continue
        if count < 3 : mRetIDs[count] = News
        count +=1
    return count
