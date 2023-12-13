"""
sqrt 구간합 문제
- N : 지점의 개수 <= 100,000 --> 제곱근 320
- mType : 도로의 종류, 추후 mTypeID인 구간의 도로의 비율을 변경할 수 있음
- mTime : 각 구간의 통과 예상시간

- init
  sqrt = 320
  sqrt_sum[]
  load[]
  load_time[]
  1. load[mID].append(도로 인덱스) --> 추후 mID에 해당되는 도로에 한번에 값 반영 가능


- update
  1. 값이 변경되면 구간합에서 변경되는 값만큼 뺴줌
  2. load_time 리스트에서 값 변경

- updateByTypme
  1. load 리스트에서 해당 인덱스의 도로의 시간에 값을 반영
  2. 값을 반영하면서 구간합의 값에도 차만큼 빼준다.
  3. res에 해당 구간의 값들을 더해서 return

- calculate
  1. mA, mB 입력 받음
  2. mA < mB면 mA = left / 아니면 mB = left 저장
  3. while을 돌려 구간합을 시작
    1. while left <= right and sqrt%left
       left +=1
       res += load_time[left]
    2. while left <= right and sqrt%right
       right -= 1
       res += load_time[right]
    3. while left <= right
       	 res += sqrt_sum[sqrt//left]
       	 left += sqrt
"""
from collections import defaultdict
def init(N:int, M:int, mType:list, mTime:list) -> None:
	"""
	  sqrt = 320
  sqrt_sum[]
  load[]
  load_time[]
  1. load[mID].append(도로 인덱스) --> 추후 mID에 해당되는 도로에 한번에 값 반영 가능
  2. sqrt_sum[]에 구간합을 반영함
	"""
	global sqrt, sqrt_sum, load, load_time
	mN = N
	sqrt = 320
	sqrt_sum = [0 for i in range(sqrt)]
	load = defaultdict(list)
	load_time = []
	for i in range(mN):
		load_time.append(mTime[i])
		load[mType[i]].append(i)
		sqrt_sum[i//sqrt] += mTime[i]
	return

def destroy() -> None:
	return

def update(mID:int, mNewTime:int) -> None:
	"""
	- update
  1. 값이 변경되면 구간합에서 변경되는 값만큼 뺴줌
  2. load_time 리스트에서 값 변경
	"""
	global sqrt, sqrt_sum, load, load_time
	sqrt_sum[mID // sqrt] += mNewTime-load_time[mID]
	load_time[mID] = mNewTime

def updateByType(mTypeID:int, mRatio256:int) -> int:
	"""
	- updateByTypme
  1. load 리스트에서 해당 인덱스의 도로의 시간에 값을 반영
  2. 값을 반영하면서 구간합의 값에도 차만큼 빼준다.
  3. res에 해당 구간의 값들을 더해서 return
	"""
	global sqrt, sqrt_sum, load, load_time

	res = 0
	for index in load[mTypeID]:
		ratio = int(load_time[index] * mRatio256 / 256)
		sqrt_sum[index // sqrt] += ratio-load_time[index]
		load_time[index] = ratio
		res += ratio
	return res

def calculate(mA:int, mB:int)-> int:
	"""
	  1. mA, mB 입력 받음
  2. mA < mB면 mA = left / 아니면 mB = left 저장
  3. while을 돌려 구간합을 시작
    1. while left <= right and sqrt%left
       left +=1
       res += load_time[left]
    2. while left <= right and sqrt%right
       right -= 1
       res += load_time[right]
    3. while left <= right
       	 res += sqrt_sum[sqrt//left]
       	 left += sqrt
	"""
	global sqrt, sqrt_sum, load, load_time
	if mA > mB:
		mA, mB = mB, mA

	left = mA
	right = mB-1


	res = 0

	while left <= right and (left)%sqrt:
		# left 0~319까지 더함
		res += load_time[left]
		left +=1
	while left <= right and (right+1)%sqrt:
		# right 639~320까지 더함
		res += load_time[right]
		right -= 1
	while left <= right:
		res += sqrt_sum[left//sqrt]
		left += sqrt

	return res
