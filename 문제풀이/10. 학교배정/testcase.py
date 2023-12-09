import sys

from solution import init, add, remove, status

CMD_INIT = 1
CMD_ADD = 2
CMD_REMOVE = 3
CMD_STATUS = 4

def run():
	q = int(input())

	mxArr = []
	myArr = []
	okay = False

	for i in range(q):
		inputarray = input().split()
		cmd = int(inputarray[0])

		if cmd == CMD_INIT:
			okay = True
			mcapa = int(inputarray[1])
			n = int(inputarray[2])
			for j in range(n):
				locinput = input().split()
				mxArr.append(int(locinput[0]))
				myArr.append(int(locinput[1]))
			init(mcapa, n, mxArr, myArr)
		elif cmd == CMD_ADD:
			mstudent = int(inputarray[1])
			mx = int(inputarray[2])
			my = int(inputarray[3])
			ans = int(inputarray[4])
			ret = add(mstudent, mx, my)
			if ans != ret:
				okay = False
		elif cmd == CMD_REMOVE:
			mstudent = int(inputarray[1])
			ans = int(inputarray[2])
			ret = remove(mstudent)
			if ans != ret:
				okay = False
		elif cmd == CMD_STATUS:
			mschool = int(inputarray[1])
			ans = int(inputarray[2])
			ret = status(mschool)
			if ans != ret:
				okay = False
		else:
			okay = False

	return okay


if __name__ == '__main__':
	sys.stdin = open('sample_input.txt', 'r')
	inputarray = input().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, TC + 1):
		score = MARK if run() else 0
		print("#%d %d" % (testcase, score), flush = True)
