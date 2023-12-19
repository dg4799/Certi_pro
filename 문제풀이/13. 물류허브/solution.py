"""
도로 이동간 최소 운송비용을 구하는 문제임.
다익스트라를 사용한다
문제를 봤을때 도로가 추가되면 다익스트라를 한번돌려서 값을 기억해둠 (인덱스별 다익스트라 결과를 list에 저장)
허브가 주어졌을때 각 인덱스부터 허브까지의 + 허브부터 인덱스까지의 거리를 더하서 결과를 도출함
add로 물류가 추가되면 다시 각인덱스별 다익스트라를 계산함 ---> 여기서 시간초과 가능....


- init
1. 도로간의 이동거리를 저장할 리스트
2. 도로간의 이동거리를 저장
3. cost 리스트 (int)

- add
1. 도로간의 이동거리를 추가 저장
2. 각 인덱스별 다익스트라를 돌려 cost 리스트에 저장

- cost
1. 입력받은 허브값 기준 각 인덱스별 허브값까지 거리를 모두 저장
2. 허브부터 각인덱스까지 거리를 모두 저장 및 return
"""
from collections import defaultdict, deque

def init(N, sCity, eCity, mCost):
	"""
	- init
1. 도로간의 이동거리를 저장할 리스트
2. 도로간의 이동거리를 저장
3. cost 리스트 (int)
	"""
	global load_list, cost_list, num, len_hub, hub_list
	hub_id = set()
	num = N
	hub_list = defaultdict(int)
	for i in range(num):
		hub_id.add(sCity[i])
		hub_id.add(eCity[i])

	hub_id = list(hub_id)
	len_hub = len(hub_id)
	idx = 1
	for i in range(len_hub):
		hub_list[hub_id[i]] = idx
		idx += 1


	load_list = defaultdict(list)

	for i in range(num):
		load_list[hub_list[sCity[i]]].append((hub_list[eCity[i]], mCost[i]))
		# load_list[eCity[i]].append((sCity[i], mCost[i]))

	cost_list = defaultdict()
	for i in range(1, len_hub+1):
		cost_list[i] = dijkstra(i)

	return len_hub
def dijkstra(start):
	global load_list, cost_list, num

	cost_if = [float("inf") for i in range(num+1)]
	Queue = deque()
	cost_if[start] = 0
	Queue.append((0, start))
	while Queue:
		dist, now = Queue.popleft()
		for i in load_list[now]:
			cost = dist + i[1]
			if cost < cost_if[i[0]]:
				cost_if[i[0]] = cost
				Queue.append((cost, i[0]))
	return cost_if


def add(sCity, eCity, mCost):
	"""
	- add
1. 도로간의 이동거리를 추가 저장
2. 각 인덱스별 다익스트라를 돌려 cost 리스트에 저장
	"""
	global load_list, cost_list, num, len_hub

	load_list[hub_list[sCity]].append((hub_list[eCity], mCost))

	cost_list = defaultdict()
	len_hub = len(load_list)
	for i in range(1, len_hub+1):
		cost_list[i] = dijkstra(i)

	return


def cost(mHub):
	global load_list, cost_list, num, len_hub
	"""
	- cost
1. 입력받은 허브값 기준 각 인덱스별 허브값까지 거리를 모두 저장
2. 허브부터 각인덱스까지 거리를 모두 저장 및 return
	"""
	global load_list, cost_list, num, hub_list

	res = 0
	for i in range(1, len_hub+1):
		res += cost_list[i][hub_list[mHub]]
		res += cost_list[hub_list[mHub]][i]




	return res