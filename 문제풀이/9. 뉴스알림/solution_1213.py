"""
mTime 시각에 뉴스채널이 뉴스를 제공 받았으면, 뉴스 채널은 등록한 유저에게 mTime+delay 시각에 뉴스 알림을 보낸다
- update를 하는데 현재 mTime이 mTime+delay보다 크거나 같으면 등록한 유저에게 뉴스알림

- init
 1. NewsChannel = dif(list) --> News[채널] = 유저
 2. update_list = {}
 2. User_news_add = dif(list)
 3. News_alam_user = dif(list)
 4. News_cancle = dif(list)

- registerUser
mTime 시각에 mUID 유저는 뉴스 알림을 받기 위해 mNum 개의 뉴스 채널 mChannelIDs[] 에 각각 등록한다.
 1. Update를 해서 뉴스알림을 먼저 보낸다
 2. NewsChannel[mChannl].append(유저)

- offerNews
 mChannel에 등록한 User 들에게 mNews를 제공함
 1. NewsChannel에서 유저들을 꺼내서
 2. 해당 유저들의 이름으로 update_list에 추가한다
  - heappush(update_list, (mTime+mDelay, mUID))
 3. News_cancle[mNews].append(유저)해서 cancleNews에서 해당 유저들에게 News 삭제
 4. len(NewsChannel[유저) return

- cancleNEws
 1. News_cancle에서 User를 찾아서 User의 News를 삭제

- checkUser
 1. update를 해서 뉴스알림을 먼저 보낸다
 2. 유저가 받은 알림의 개수는 0개로 초기화
 3. 유저가 받은 알림의 개수를 return


- update
 1. mTime 시각을 받아서
 2. News_offer for문을 돌려서
 3. mTime이 mTime + mDelay 보다 갖거나
 4. User[유저].append(mNews)

"""
from collections import defaultdict
from heapq import heappop, heappush


def init(N: int, K: int) -> None:
    """
    - init
 1. NewsChannel = dif(list) --> News[채널] = 유저
 2. update_list = {}
 2. User_news_add = dif(list)
 3. News_alam_user = dif(list)
 4. News_cancle = dif(list)
    """
    global News_Channel, update_list, User_news_add, News_cancle
    News_cancle = set()
    News_Channel = defaultdict(list)
    update_list = []
    User_news_add = defaultdict(list)


def offerNews(mTime: int, mNewsID: int, mDelay: int, mChannelID: int) -> int:
    """
    - offerNews
 mChannel에 등록한 User 들에게 mNews를 제공함
 1. NewsChannel에서 유저들을 꺼내서
 2. 해당 유저들의 이름으로 update_list에 추가한다
  - heappush(update_list, (mTime+mDelay, mUID))
 3. News_cancle[mNews].append(유저)해서 cancleNews에서 해당 유저들에게 News 삭제
 4. len(NewsChannel[유저) return
    """
    global News_Channel, update_list, User_news_add, News_cancle

    heappush(update_list, (mTime + mDelay, mNewsID, mChannelID))
    return len(News_Channel[mChannelID])


def registerUser(mTime: int, mUID: int, mNum: int, mChannelIDs: list) -> None:
    """
    - registerUser
mTime 시각에 mUID 유저는 뉴스 알림을 받기 위해 mNum 개의 뉴스 채널 mChannelIDs[] 에 각각 등록한다.
 1. Update를 해서 뉴스알림을 먼저 보낸다
 2. NewsChannel[mChannl].append(유저)
    """
    global News_Channel, update_list, User_news_add, News_alam_user, News_cancle

    update(mTime)

    for i in range(mNum):
        News_Channel[mChannelIDs[i]].append(mUID)


def update(mTime_current):
    global update_list


    while update_list and update_list[0][0] <= mTime_current:
        Time, mNewsID, mChannelID = heappop(update_list)
        if mNewsID in News_cancle: continue
        for User in News_Channel[mChannelID]:
            User_news_add[User].append(mNewsID)


def cancelNews(mTime: int, mNewsID: int) -> None:
    """
    - cancleNEws
 1. News_cancle에서 User를 찾아서 User의 News를 삭제
    """
    News_cancle.add(mNewsID)


def checkUser(mTime: int, mUID: int, mRetIDs: list) -> int:
    """
    - checkUser
 1. update를 해서 뉴스알림을 먼저 보낸다
 2. 유저가 받은 알림의 개수는 0개로 초기화
 3. 유저가 받은 알림의 개수를 return
    """
    update(mTime)



    count = 0
    while len(User_news_add[mUID]) != 0:
        News = User_news_add[mUID].pop(-1)
        if News in News_cancle: continue
        if count < 3: mRetIDs[count] = News
        count += 1
    return count