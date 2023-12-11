import sys
import solution

CMD_INIT = 100
CMD_UPDATE_SCORE = 200
CMD_UNION_TEAM = 300
CMD_GET_SCORE = 400


def run():
    ok = False
    queryCnt = int(input())
    for i in range(queryCnt):
        cmd, *r = map(int, input().split())
        if cmd == CMD_INIT:
            solution.init(*r)
            ok = True
        if cmd == CMD_UPDATE_SCORE:
            mWinnerID, mLoserID, mScore = r
            solution.updateScore(mWinnerID, mLoserID, mScore)
        if cmd == CMD_UNION_TEAM:
            mPlayerA, mPlayerB = r
            solution.unionTeam(mPlayerA, mPlayerB)
        if cmd == CMD_GET_SCORE:
            mID, ans = r
            ret = solution.getScore(mID)
            if ans != ret:
                ok = False
    return ok


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    TC, MARK = map(int, input().split())

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
