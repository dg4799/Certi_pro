import sys
# from solution import init, add, distance
from solution_self import init, add, distance
# from solution_1 import init, add, distance

CMD_INIT     = 0
CMD_ADD      = 1
CMD_DISTANCE = 2

def run():
    len = int(sys.stdin.readline())

    for i in range(len):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            N = int(next(inputs))
            Range = int(next(inputs))
            map = []
            for j in range(N):
                inputs2 = iter(sys.stdin.readline().split())
                row = [int(val) for val in inputs2]
                map.append(row)
            init(N, Range, map)
            ret_val = 1

        elif cmd == CMD_ADD:
            id = int(next(inputs))
            r = int(next(inputs))
            c = int(next(inputs))
            ret = add(id, r, c)

        elif cmd == CMD_DISTANCE:
            id = int(next(inputs))
            id2 = int(next(inputs))
            ret = distance(id, id2)
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