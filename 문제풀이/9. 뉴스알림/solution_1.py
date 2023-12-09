# timeflow대로 문제가 흘러가고, 이때 중요한 건
# 1. 무엇을 update할 것인지
# 2. update하는 시점

# 처음엔 offernews 들어오면 user별 max_heap에 넣고 check_user 들어오면 heappop해서
# 1. mTime보다 크면 temps에 저장 (나중에 다시 넣기)
# 2. 삭제된 건지 판별

# update할 heap을 하나 만들어주고 필요한 시점마다 시간 비교해서 뺼 것만 빼주는 게 가장 효율적
# 그니까 update가 필요할 때만 해주면 되는 것

from collections import defaultdict
import heapq as hq

global user_news, channels, update_list, deleted_news


def update(mTime):  # 업데이트 함수 너무 최고다, 언제 불릴지 잘 판단하기
    while update_list and update_list[0][0] <= mTime:

        min_time, mNewsID, channel_id = hq.heappop(update_list)
        if mNewsID in deleted_news: continue

        for user in channels[channel_id]:  # 구독자가 없는 채널은 없음
            user_news[user].append(mNewsID)


def init(N, K):
    global user_news, channels, update_list, deleted_news
    user_news = defaultdict(list)  # userid: [newsid] --> 유저가 받은 뉴스 알림 저장, 어차피 최신순으로 저장됨, 삭제된 것도 가지고 있을 수 있음
    channels = {}  # channel id: [userid] #채널이 갖고 있는 유저 id들 저장
    update_list = []  # min_heap, (mTime+mDelay, newsID, channelID)
    deleted_news = set()  # 삭제된 news들 제거


def registerUser(mTime, mUID, mNum, mGroupIDs):
    update(mTime)  # heap에 저장되어 있는 알림들 user에게 업데이트 --> 업데이트 되고 user가 채널 목록에 들어가야 하기 때문
    # mtime+mdealy에 추가되는 유저는 어차피 그 시간 뉴스 못 받음

    for channel_id in mGroupIDs[:mNum]:  # argument로 주어지는 놈들 인덱스 딱 안 맞을 수도 있음, print 찍어보거나 main 보기 (섬지키기와 동일)
        if channel_id in channels:
            channels[channel_id].append(mUID)
        else:
            channels[channel_id] = [mUID]  ### channel id에 굳이 news_id들도 가지고 있을 필요 있나? --> 필요 없음
    return None


def offerNews(mTime, mNewsID, mDelay, mGroupID):
    hq.heappush(update_list, (mTime + mDelay, mNewsID, mGroupID))
    return len(channels[mGroupID])


def cancelNews(mTime, mNewsID):
    deleted_news.add(mNewsID)
    return


def checkUser(mTime, mUID, mRetIDs):
    update(mTime)

    k = 0
    while user_news[mUID]:
        news_id = user_news[mUID].pop(-1)
        if news_id in deleted_news: continue
        if k <= 2: mRetIDs[k] = news_id
        k += 1
    return k