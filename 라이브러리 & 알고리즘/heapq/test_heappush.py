

list_1 = [(5,1,1,0),(0,1,1,3),(0,1,4,0),(0,2,1,0),(1,0,5,0),(0,2,0,0),(0,0,0,0),(0,1,0,0),(0,0,3,0),(0,0,0,4),(0,1,1,0)]


import heapq

check = []
for i in list_1:
    heapq.heappush(check, i)

for i in range(len(check)):
    print(heapq.heappop(check))