import sys
from solution_self import init, writeMessage, commentTo, erase, getBestMessages, getBestUsers
# from solution_2 import init, writeMessage, commentTo, erase, getBestMessages, getBestUsers

CMD_INIT = 100
CMD_WRITE_MESSAGE = 200
CMD_COMMENT_TO = 300
CMD_ERASE = 400
CMD_GET_BEST_MESSAGES = 500
CMD_GET_BEST_USERS = 600


def run():
    Q = int(input())
    okay = False

    mBestUserList = [None for _ in range(5)]
    mBestMessageList = [0 for _ in range(5)]

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            init()
            okay = True
        elif cmd == CMD_WRITE_MESSAGE:
            mUser = next(input_iter)
            mID = int(next(input_iter))
            mPoint = int(next(input_iter))
            ret = writeMessage(mUser, mID, mPoint)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_COMMENT_TO:
            mUser = next(input_iter)
            mID = int(next(input_iter))
            mTargetID = int(next(input_iter))
            mPoint = int(next(input_iter))
            ret = commentTo(mUser, mID, mTargetID, mPoint)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_ERASE:
            mID = int(next(input_iter))
            ret = erase(mID)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_GET_BEST_MESSAGES:
            getBestMessages(mBestMessageList)
            for i in range(5):
                ans = int(next(input_iter))
                if mBestMessageList[i] != ans:
                    okay = False
        elif cmd == CMD_GET_BEST_USERS:
            getBestUsers(mBestUserList)
            for i in range(5):
                ans = next(input_iter)
                if mBestUserList[i] != ans:
                    okay = False
        else:
            okay = False
    return okay


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)
