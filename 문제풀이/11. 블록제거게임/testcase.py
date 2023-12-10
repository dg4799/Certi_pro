import sys
from solution_1 import init, dropBlocks, removeBlocks

CMD_INIT = 100
CMD_DROP = 200
CMD_REMOVE = 300


def run():
    query = int(input())
    ok = False
    for i in range(query):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            R = int(next(input_iter))
            C = int(next(input_iter))
            init(R, C)
            ok = True
        elif cmd == CMD_DROP:
            mTimestamp = int(next(input_iter))
            mCol = int(next(input_iter))
            mLen = int(next(input_iter))
            ret = dropBlocks(mTimestamp, mCol, mLen)
            ans = int(next(input_iter))
            if ans != ret:
                ok = False
        elif cmd == CMD_REMOVE:
            mTimestamp = int(next(input_iter))
            ret = removeBlocks(mTimestamp)
            ans = int(next(input_iter))
            if ans != ret:
                ok = False
    return ok


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
