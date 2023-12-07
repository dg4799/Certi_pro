from heapq import heappop, heappush

# heap에 원소 추가
heap = []
values = [4, 1, 3, 7, 9]

for i in values:
    heappush(heap, i)
print(heap)


# 최소 힙 출력
heap = []
values = [4, 1, 3, 7, 9]
for i in range(len(heap)):
    print(heappop(heap))            # 가장 작은 원소부터 제거하는 heappop 사용


# 최대 힙 출력
heap = []
values = [4, 1, 3, 7, 9]

for i in values:
    heappush(heap, -i)              # -를 붙여 숫자를 추가하고

for i in range(len(heap)):
    print(-heappop(heap))           # -가 붙어서 가장 큰숫자가 가장 작은 숫자가 되어 heappop에 의해 제거되는데 이를 출력
                                    # 이때 다시 부호를 -로 바꿔주면 가장 큰 숫자부터 출력됨