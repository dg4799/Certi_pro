from typing import List
import heapq as hq

global id_name, papers, comments, recomments, user_max_heap, paper_max_heap
from collections import defaultdict


def init() -> None:
    global id_name, papers, comments, recomments, user_max_heap, paper_max_heap

    # 사용자의 총합 포인트를 만들기 위한 dict (wirteMessage return)
    id_name = defaultdict(int)  # name:총 포인트
    # 글의 총합 포인트를 만들기 위한 dict (commentTo return)
    papers = {}  # mid: [0:작성자 id, 1:글 총합point,2:글 자체 point, 3:childrens[]] #children에는 댓글만 담김(대댓글은 안 넣음)
    comments = {}  # mid: [0:작성자 id, 1:댓글point, 2:childrens[], 3:parent_paper]
    recomments = {}  # mid: [0:작성자 id, 1:대댓글point, 2:parent_comment]
    user_max_heap = []  # (-총합 포인트, 영어이름)
    paper_max_heap = []  # (-총합 포인트, mid)


def writeMessage(mUser: str, mID: int, mPoint: int) -> int:
    # 글 작성자 점수 부여
    id_name[mUser] += mPoint
    # 글 리스트에 추가
    papers[mID] = [mUser, mPoint, mPoint, []]

    hq.heappush(user_max_heap, (-id_name[mUser], mUser))
    hq.heappush(paper_max_heap, (-papers[mID][1], mID))

    return id_name[mUser]


def commentTo(mUser: str, mID: int, mTargetID: int, mPoint: int) -> int:
    # 댓글 작성자 점수 부여
    id_name[mUser] += mPoint
    hq.heappush(user_max_heap, (-id_name[mUser], mUser))

    # 타겟 글에 달린 댓글인 경우, 타겟의 paper를 뽑음
    if mTargetID in papers:
        # 타겟 글에 총합 포인트 더해주기
        papers[mTargetID][1] += mPoint
        # 타겟 글에 자식 넣어주기
        papers[mTargetID][3].append(mID)
        hq.heappush(paper_max_heap, (-papers[mTargetID][1], mTargetID))
        # 댓글 리스트에 추가
        comments[mID] = [mUser, mPoint, [], mTargetID]
        # 타겟글(댓글 또는 답글이 달린 글의 총합 포인트 return)
        return papers[mTargetID][1]

    # 어떤 글의 댓글에 달린 대댓글인 경우
    elif mTargetID in comments:
        # 타겟 글의 id를 뽑음
        parent_paper_id = comments[mTargetID][3]
        # 타겟 글에 총합 포인트를 더해줌
        papers[parent_paper_id][1] += mPoint
        hq.heappush(paper_max_heap, (-papers[parent_paper_id][1], parent_paper_id))
        # 타겟 댓글의 자식에 넣어주기
        comments[mTargetID][2].append(mID)
        # 대댓글 리스트에 추가
        recomments[mID] = [mUser, mPoint, mTargetID]
        # 타겟글의 총합 포인트 return
        return papers[parent_paper_id][1]


def erase(mID: int) -> int:
    # 글 자체를 지우는 것이면
    if mID in papers:
        # 글 작성자 점수 업데이트
        id_name[papers[mID][0]] -= papers[mID][2]
        hq.heappush(user_max_heap, (-id_name[papers[mID][0]], papers[mID][0]))
        # 글의 점수 삭제
        papers[mID][1] = 0
        hq.heappush(paper_max_heap, (-papers[mID][1], mID))  # 글

        # 글에 달린 댓글 손보기
        for child_of_paper in papers[mID][3]:
            # 댓글 작성자 점수 업데이트
            id_name[comments[child_of_paper][0]] -= comments[child_of_paper][1]
            hq.heappush(user_max_heap, (-id_name[comments[child_of_paper][0]], comments[child_of_paper][0]))

            # 댓글에 달린 대댓글 손보기
            for child_of_comment in comments[child_of_paper][2]:
                # 대댓글 작성자 점수 업데이트
                id_name[recomments[child_of_comment][0]] -= recomments[child_of_comment][1]
                hq.heappush(user_max_heap, (-id_name[recomments[child_of_comment][0]], recomments[child_of_comment][0]))
        # 해당 글을 작성한 사용자의 총합포인트 return
        return id_name[papers[mID][0]]


    # 댓글 하나를 지우는 것이라면
    elif mID in comments:
        # 댓글 작성자 점수 업데이트
        id_name[comments[mID][0]] -= comments[mID][1]
        hq.heappush(user_max_heap, (-id_name[comments[mID][0]], comments[mID][0]))

        # 댓글의 부모번호 뽑기
        parent_of_comment = comments[mID][3]
        # 글 총합 점수에서 댓글 포인트 만큼 빼기
        papers[parent_of_comment][1] -= comments[mID][1]

        # 댓글에 달린 답글 손보기
        for child_of_comment in comments[mID][2]:  # 대댓글 관리
            # 대댓글 작성자 점수 업데이트
            id_name[recomments[child_of_comment][0]] -= recomments[child_of_comment][1]
            hq.heappush(user_max_heap, (-id_name[recomments[child_of_comment][0]], recomments[child_of_comment][0]))
            # 글 총합점수에서 대댓글 점수 빼주기
            papers[parent_of_comment][1] -= recomments[child_of_comment][1]

        # 글에 달린 댓글 삭제
        papers[parent_of_comment][3].remove(mID)  # 자식 삭제해주기 --> Q1. 이부분  child를 set으로 만들어서 더 최적화 할 껄 그럤나?
        hq.heappush(paper_max_heap, (-papers[parent_of_comment][1], parent_of_comment))  # 글
        # 댓글 또는 답글이 달려 있던 글의 총합 포인트 return
        return papers[parent_of_comment][1]


    # 대댓글 삭제할 때
    elif mID in recomments:
        # 대댓글 작성자 업데이트
        id_name[recomments[mID][0]] -= recomments[mID][1]
        hq.heappush(user_max_heap, (-id_name[recomments[mID][0]], recomments[mID][0]))
        # 부모의 부모 타고 올라가서 부모 글 찾기
        paper_parent = comments[recomments[mID][2]][3]
        # 글의 총합포인트에서 점수 뺴기
        papers[paper_parent][1] -= recomments[mID][1]
        hq.heappush(paper_max_heap, (-papers[paper_parent][1], paper_parent))
        # 자식 삭제해주기
        comments[recomments[mID][2]][2].remove(mID)
        # 댓글 또는 답글이 달려 있던 글의 총합 포인트 return
        return papers[paper_parent][1]


def getBestMessages(mBestMessageList: List[int]) -> None:

    # 탑 5를 고르기 위한 임시폴더 생성
    temps = []
    # 임시폴더에 5개가 추가될때까지 while
    while len(temps) != 5:
        # 글_max 리스트에서 하나씩 뽑음(스코어가 음수여서 가장 높은 스코어 부터 pop)
        temp = hq.heappop(paper_max_heap)
        # 스코어와 mID를 뽑는다
        score, mID = -temp[0], temp[1]
        # 스코어가 해당 mID의 총합과 같지 않으면 무시 (글의 mID 총합과 같지 않는다 => 더 낮다)
        # 이미 해당 점수와 mID가 temps에 있으면 무시 (중복제거)
        if score != papers[mID][1] or temp in temps: continue
        # 해당 temp를 추가
        temps.append(temp)

    i = 0
    # 탑 5개를 뽑은 temps에서 score와 mID를 뽑아서
    for score, mID in temps:
        # 탑 5개의 리스트를 다시 paper_max_heap에 업데이트
        hq.heappush(paper_max_heap, (score, mID))
        # return값인 mBestMessageList에 인덱스별 mID를 입력함.
        mBestMessageList[i] = mID
        i += 1

    return


def getBestUsers(mBestUserList: List[str]) -> None:
    # 위와 동일
    temps = []
    while len(temps) != 5:
        temp = hq.heappop(user_max_heap)
        score, name = -temp[0], temp[1]
        # 스코어가 해당 mID의 총합과 같지 않으면 무시 (글의 mID 총합과 같지 않는다 => 더 낮다)
        # 이미 해당 점수와 mID가 temps에 있으면 무시 (중복제거)
        if score != id_name[name] or temp in temps: continue

        temps.append(temp)

    # 위와 동일
    i = 0
    for score, name in temps:
        hq.heappush(user_max_heap, (score, name))
        mBestUserList[i] = name
        i += 1

    return