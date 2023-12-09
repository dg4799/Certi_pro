import sys
# from solution_1 import init, registerUser, offerNews, cancelNews, checkUser
from solution_self import init, registerUser, offerNews, cancelNews, checkUser

CMD_INIT = 0
CMD_REGI = 1
CMD_OFFER = 2
CMD_CANCEL = 3
CMD_CHECK = 4

gids = [0 for _ in range(30)]
ansids = [0 for _ in range(3)]
retids = [0 for _ in range(3)]

def run():
    isOK = False
    C = int(sys.stdin.readline())
    for c in range(C):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))
        if cmd == CMD_INIT:
            N = int(next(inputs))
            K = int(next(inputs))
            init(N, K)
            isOK = True
        elif cmd == CMD_REGI:
            time = int(next(inputs))
            uid = int(next(inputs))
            num = int(next(inputs))
            for i in range(num):
                gids[i] = int(next(inputs))
            registerUser(time, uid, num, gids)
        elif cmd == CMD_OFFER:
            time = int(next(inputs))
            nid = int(next(inputs))
            delay = int(next(inputs))
            gid = int(next(inputs))
            ret = offerNews(time, nid, delay, gid)
            ans = int(next(inputs))
            if ret != ans:
                isOK = False
        elif cmd == CMD_CANCEL:
            time = int(next(inputs))
            nid = int(next(inputs))
            cancelNews(time, nid)
        elif cmd == CMD_CHECK:
            time = int(next(inputs))
            uid = int(next(inputs))
            ret = checkUser(time, uid, retids)
            ans = int(next(inputs))
            num = ans
            if num > 3:
                num = 3
            for i in range(num):
                ansids[i] = int(next(inputs))
            if ret != ans:
                isOK = False
            for m in range(num):
                if ansids[m] != retids[m]:
                    isOK = False
        else:
            isOK = False
    return isOK


if __name__ == '__main__':
    import time
    sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    start = time.time()
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
    end = time.time()

    print(end-start)
