import sys
from solution_self import init, addSample, deleteSample, predict

CMD_INIT = 100
CMD_ADD_SAMPLE = 200
CMD_DELETE_SAMPLE = 300
CMD_PREDICT = 400


def run():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            K = int(next(input_iter))
            L = int(next(input_iter))
            init(K, L)
            okay = True
        elif cmd == CMD_ADD_SAMPLE:
            mID = int(next(input_iter))
            mX = int(next(input_iter))
            mY = int(next(input_iter))
            mC = int(next(input_iter))
            addSample(mID, mX, mY, mC)
        elif cmd == CMD_DELETE_SAMPLE:
            mID = int(next(input_iter))
            deleteSample(mID)
        elif cmd == CMD_PREDICT:
            mX = int(next(input_iter))
            mY = int(next(input_iter))
            ret = predict(mX, mY)
            ans = int(next(input_iter))
            if ret != ans:
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
