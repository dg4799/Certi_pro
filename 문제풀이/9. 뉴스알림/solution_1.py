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


def update(mTime):
    # registerUser와 checkUser시에 업데이트 함수 부르기 (이거 계속 확인해보기.....)
    # heap인 update_list에 mTime에 육박한 리스트가 있으면 update 시작 (인덱스 에러를 피하기 위해 update_list가 0개가 아닐때 병행조건)
    while len(update_list) != 0 and update_list[0][0] <= mTime:

        # update_list에서 가장 빠른 mTime 작업을 pop으로 뽑아옴
        min_time, mNewsID, channel_id = hq.heappop(update_list)
        # 해당 뉴스가 mNewsID에 있으면 무시
        if mNewsID in deleted_news: continue

        # 해당 채널의 구독자를 뽑아서
        for user in channels[channel_id]:  # 구독자가 없는 채널은 없음
            # 유저의 뉴스알림 리스트에 뉴스 추가
            user_news[user].append(mNewsID)


def init(N, K):
    global user_news, channels, update_list, deleted_news
    user_news = defaultdict(list)  # userid: [newsid] --> 유저가 받은 뉴스 알림 저장, 어차피 최신순으로 저장됨, 삭제된 것도 가지고 있을 수 있음
    channels = {}  # channel id: [userid] #채널이 갖고 있는 유저 id들 저장
    update_list = []  # min_heap, (mTime+mDelay, newsID, channelID)
    deleted_news = set()  # 삭제된 news들 제거


def registerUser(mTime, mUID, mNum, mGroupIDs):
    # mTime 시각에 유저에게 보내지는 뉴스 알림이 있는 경우 먼저 알림을 보내기 위한 update
    update(mTime)

    # mGroupIDs를 받아서 뉴스채널에 유저를 등록한다.
    for channel_id in mGroupIDs[:mNum]:
        # channels 리스트에 있으면 리스트에 mUID append
        if channel_id in channels:
            channels[channel_id].append(mUID)
        # channles 리스트에 없으면 channels[GroupID] = [mUID] 저장, 같은 채널에 mUID가 여러개 들어올 수 있어서 []로 저장함
        else:
            channels[channel_id] = [mUID]
    return

def offerNews(mTime, mNewsID, mDelay, mGroupID):
    # update_list에 정보를 넣고 시간대별로 update해서 반영
    hq.heappush(update_list, (mTime + mDelay, mNewsID, mGroupID))
    return len(channels[mGroupID])


def cancelNews(mTime, mNewsID):
    # cancle 뉴스를 받아서 delete_news에 추가 (향후 checkUser에서 삭제된 뉴스 알림은 제외하기 위함)
    # mNewsID는 중복으로 주어지지 않아서 모두 넣고 체크하면 됨.
    deleted_news.add(mNewsID)
    return


def checkUser(mTime, mUID, mRetIDs):
    # mTime 시각에 유저에게 보내지는 뉴스 알림이 있는 경우 먼저 알림을 보내기 위한 update
    update(mTime)

    count = 0
    while user_news[mUID]:
        # 유저의 알림을 받는 뉴스를 꺼내서
        news_id = user_news[mUID].pop()
        # 해당 뉴스가 cancle 뉴스에 포함되어 있으면 무시 (뉴스id는 중복되지 않기 때문)
        if news_id in deleted_news: continue
        # cancle 뉴스에 포함되어있지 않다면 받은 뉴스 ID를 최신순서대로 저장 (최대 3개까지만 넣기위해 count를 넣음)
        if count <= 2: mRetIDs[count] = news_id
        count += 1
    return count