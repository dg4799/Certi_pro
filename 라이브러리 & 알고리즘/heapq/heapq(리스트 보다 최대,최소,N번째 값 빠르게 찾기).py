"""
heapq을 사용하는 이유
- 최대값, 최소값, N번째 값 등 빠르게 원소를 탐색할 수 있음.
- heappush로 리스트에 heap을 추가하고, heappop으로 가장 작은 원소를 찾는 방법으로 활용

리스트의 최대값, 최소값, N번째 값 등등 시간 복잡도 O(N)
heap의 시간 복잡도 O(1)
"""

# [ 힙에 원소 추가 ]
from heapq import heappush, heappop
heap = []
values = [4, 1, 3, 7, 9]

for i in values:
    heappush(heap, i)
print(heap)

"""
     1  ---> root
   /  \
  3     5
 / \   /  \
4   8 7

[1, 3, 5, 4, 8, 7]

노드는 어디에 있든지 자식의 두 노드볻 작아야함.
이 규칙으로 원소들은 배열됨.
"""
print("--------------------------------------")




# [ 힙에서 원소 삭제 ]
heappop(heap) # root에서 가장 작은 원소를 삭제함
print(heap)
heappop(heap)
print(heap)
heappop(heap)
print(heap)
"""
heap에서는 원소가 사라질때마다 재배치가 됨.
"""
print("--------------------------------------")


# [ 기존 리스트를 힙으로 변환 ]
from heapq import heapify

heap = [4, 1, 7, 3, 8, 5]
heapify(heap)
print(heap)

nums = [4, 1, 7, 3, 8, 5]
heap = nums[:]
heapify(heap)
print(nums)
print(heap)
"""
heapify는 인자로 넘긴 리스트에 직접 변경을 가함. 원본 리스트의 형태를 보존해야하는 경우에는
해당 리스트를 복제한 후에 넘겨야 함.
"""
print("--------------------------------------")


# [ 최소 힙 ]
heap = []
values = [1,5,3,2,4]
for i in values:        # for문을 실행하고 나면 heap은 [1,2. 출근길 라디오,3,5,4]로 힙 정렬이 되게 된다.
    heappush(heap, i)

for i in range(len(values)):          # heappop으로 원소중 가장 작은것만 제거는 것이라서 작은 숫자 순서대로 1,2. 출근길 라디오,3,4,5가 출력된다.
    print(heappop(heap))

"""
0은 heap에서 가장 앞의(작은) 원소임, 그러나 1, 2. 출근길 라디오 인덱스의 값은 순서대로 되어있지 않을 수 있음.
왜냐하면 힙은 자식 노드보다 작은것만 만족하면 되기 때문.
"""
print("--------------------------------------")


# [ 최대 힙 ]
heap = []
values = [1,5,3,2,4]

for i in values:            # for문을 실행시키고 나면 heap은 [-5,-4,-3,-1,-2. 출근길 라디오]가 된다.
    heappush(heap, -i)
"""
heap에 push할때 부호를 바꿔서 넣으면 가장 큰숫자에 -가 붙어 -가 붙은 큰숫자가 맨앞에 오고
이후 heap 구조로 배열됨
"""

for i in range(len(heap)):          # for문을 실행시키면 5,4,3,2. 출근길 라디오,1이 출력된다. 즉, 큰 숫자부터 출력이 된다.
    print(-heappop(heap))
"""
다시 heappop으로 가장 작은 원소부터 제거하는데 -가 붙은 큰숫자가 가장 작은 숫자이기 때문에
가장 작은숫자인 -가 붙은 큰숫자를 하나씩 제거하며 출력할때 다시 부호를 바꿔주면 가장 큰숫자가 출력됨
"""

# 결국 heappop으로 가장 작은 원소를 뽑는데 이때 -로 push해서 가장 큰숫자가 작은숫자가 되게해서 뽑으면 최대값
# 그냥 push해서 heappop으로 뽑으면 작은 숫자가 뽑혀서 최소값임
print("--------------------------------------")


# [ n번째 최소값 ]
def min_heap_num(values, n):
    heap = []
    for i in values:                # values를 받아서 heap에 push
        heappush(heap, i)

    for i in range(n):            # 가장 작은 원소를 제거하는 heappop을 num만큼 for문을 돌리면
        min_num = heappop(heap)     # for문이 돌때마다 가장 작은 원소가 제거되며 변수에 저장됨

    return min_num
"""
입력받은 n만큼 for문으로 heappop을 하면
n번째 숫자가 가장 작은 숫자가 되어 최소값을 뽑을 수 있음.
"""

values = [4,8,3,2,1]
print(min_heap_num(values, 2))
print("--------------------------------------")

# [ n번째 최대값 ]
def max_heap_num(values, n):
    heap = []
    for i in values:                # values를 받아서 heap에 push할때 -를 붙여 푸시
        heappush(heap, -i)

    for i in range(n):
        max_num = -heappop(heap)    # -가 붙어서 가장 큰숫자가 가장 작은 숫자가 되어 heappop에 의해 제거되며 변수에 저장
                                    # 이때 다시 부호를 -로 바꿔주면 가장 큰 숫자부터 출력됨
    return max_num
"""
heappush 할때 숫자에 -를 붙여 heappop을 할때 가장 큰 숫자가 가장 작은 숫자가 되게 하고
입력받은 n만큼 for문으로 heappop을 하면
n번째 가장 작은 숫자(-가 붙은 가장 큰 숫자)를 다시 부호를 바꾸면 가장 큰 숫자가 되어 n번째 최대값을 뽑을 수 있음.
"""
values = [4,8,3,2,1]
print(max_heap_num(values, 1))
print("--------------------------------------")


# [ 힙 정렬(작은순) ]
def heap_sort_min(values):
    heap = []
    for i in values:
        heappush(heap, i)

    sorted_values = []
    while heap:
        sorted_values.append(heappop(heap))     # heappop으로 가장 작은 숫자를 sroted_values에 append
    return sorted_values

values = [4,8,3,2,1]
print(heap_sort_min(values))


# [ 힙 정렬(큰순) ]
def heap_sort_max(values):
    heap = []
    for i in values:
        heappush(heap, -i)

    sorted_values = []
    while heap:
        sorted_values.append(-heappop(heap))     # 부호를 다시 바꿔 큰숫자부터 append 됨.
    return sorted_values

values = [4,8,3,2,1]
print(heap_sort_max(values))
