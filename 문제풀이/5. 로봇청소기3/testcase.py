import sys
from solution_2 import init, cleanHouse

global MAX_N, mLimitMoveCnt, houseInfo, isCleaned, robotInfo, moveRobotsCallCnt

MAX_N = 30
mLimitMoveCnt = 0;
houseInfo = [[0 for _ in range(MAX_N)] for _ in range(MAX_N)]
isCleaned = [[0 for _ in range(MAX_N)] for _ in range(MAX_N)]
robotInfo = [0, 0, 0]
moveRobotsCallCnt = 0;

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def scanFromRobot(floorState) -> None:
    global robotInfo
    robot_y = robotInfo[0];
    robot_x = robotInfo[1];
    direction = robotInfo[2];

    if direction == 0:  # UP
        y = robot_y - 1
        for sy in range(0, 3):
            x = robot_x - 1
            for sx in range(0, 3):
                floorState[sy][sx] = houseInfo[y][x]
                x += 1
            y += 1
    elif direction == 1:  # LEFT
        y = robot_y - 1
        for sx in range(2, -1, -1):
            x = robot_x - 1
            for sy in range(0, 3):
                floorState[sy][sx] = houseInfo[y][x]
                x += 1
            y += 1
    elif direction == 2:  # DOWN
        y = robot_y - 1
        for sy in range(2, -1, -1):
            x = robot_x - 1
            for sx in range(2, -1, -1):
                floorState[sy][sx] = houseInfo[y][x]
                x += 1
            y += 1
    elif direction == 3:
        y = robot_y - 1
        for sx in range(0, 3):
            x = robot_x - 1
            for sy in range(2, -1, -1):
                floorState[sy][sx] = houseInfo[y][x]
                x += 1
            y += 1
    return


def moveRobot(mCommand: int) -> int:
    global moveRobotsCallCnt, robotInfo, dy, dx, isCleaned
    moveRobotsCallCnt += 1
    if mCommand < 0 or mCommand >= 4:
        return 0;

    next_dir = (robotInfo[2] + mCommand) % 4;

    sy = robotInfo[0] + dy[next_dir];
    sx = robotInfo[1] + dx[next_dir];

    if houseInfo[sy][sx] == 1:
        return 0;
    else:
        robotInfo[0] = sy;
        robotInfo[1] = sx;
        robotInfo[2] = next_dir;
        isCleaned[sy][sx] = 1;
    return 1;


def run() -> None:
    global isCleaned, houseInfo, robotInfo, moveRobotsCallCnt, mLimitMoveCnt
    inputs = iter(sys.stdin.readline().split())
    N = int(next(inputs))
    subTaskCount = int(next(inputs))

    init(N, subTaskCount);
    ok = True;

    for subtask in range(subTaskCount):
        for y in range(N):
            inputs = iter(sys.stdin.readline().split())
            for x in range(N):
                houseInfo[y][x] = int(next(inputs))
                isCleaned[y][x] = 0;

        inputs = iter(sys.stdin.readline().split())
        robotInfo[0] = int(next(inputs))
        robotInfo[1] = int(next(inputs))
        robotInfo[2] = int(next(inputs))
        mLimitMoveCnt = int(next(inputs))
        isCleaned[robotInfo[0]][robotInfo[1]] = 1;
        moveRobotsCallCnt = 0;
        cleanHouse(mLimitMoveCnt, scanFromRobot, moveRobot);

        if mLimitMoveCnt < moveRobotsCallCnt:
            ok = False;

        for y in range(N):
            for x in range(N):
                if houseInfo[y][x] == 1:
                    continue
                if isCleaned[y][x] == 0:
                    ok = False
    return ok;


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
