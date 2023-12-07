import sys
from solution_self import init, add, distance, count

CMD_INIT = 100
CMD_ADD = 200
CMD_DISTANCE = 300
CMD_COUNT = 400


def run():
    len = int(sys.stdin.readline())

    for i in range(len):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            mName1 = str(next(inputs))
            mDay1 = int(next(inputs))
            init(mName1, mDay1)
            ret_val = 1

        elif cmd == CMD_ADD:
            mName1 = str(next(inputs))
            mName2 = str(next(inputs))
            mDay1 = int(next(inputs))
            mDay2 = int(next(inputs))
            ret = add(mName1, mName2, mDay1, mDay2)
            ans = int(next(inputs))
            if ret != ans:
                ret_val = 0

        elif cmd == CMD_DISTANCE:
            mName1 = str(next(inputs))
            mName2 = str(next(inputs))
            ret = distance(mName1, mName2)
            ans = int(next(inputs))
            if ret != ans:
                ret_val = 0

        elif cmd == CMD_COUNT:
            mDay1 = int(next(inputs))
            ret = count(mDay1)
            ans = int(next(inputs))
            if ret != ans:
                ret_val = 0

    return ret_val


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
