"""
bisect는 이진 탐색을 구현한 함수임
- 이진 탐색이란 찾고자하는 특정한 값을 가운데 값을 찾아 비교하고 크면 가운데 우측들의 값에서부터 다시 가운데를 찾아 비교
- 0번 인덱스부터 N번 인덱스까지 값을 찾는 방식은 시간복잡도 O(N)
- 이진 탐색은 시간복잡도 O(logN)

참고 : https://kangworld.tistory.com/65'


bisect_left(arr, 5) : arr 배열에서 5를 찾아 왼쪽의 인덱스를 반환
bisect_right(arr, 5) : arr 배열에서 5를 찾아 오른쪽의 인덱스를 반환
insort(arr, 2) : 정렬된 arr 배열에서 2가 들어갈 자리를 찾아 arr에 값 2를 삽입함.
"""
"""
[0, 1, 2. 출근길 라디오, 3, 4, 5, 6, 7, 8, 9] 의 정렬된 배열이 있을 때,
현재 정렬된 상태를 유지하면서 n = 5 이라는 요소를 배열에 추가하고 싶다고 해봅시다.
어떤 인덱스에 넣어야하는지 계산하는 함수를 구해봅시다.
"""

# 이진 탐색을 사용하지 않고 구현 : 시간복잡도 O(N)
nums = [0,1,2,3,4,5,6,7,8,9]
n = 5
for i in range(len(nums)):
    if n <= nums[i]:
        break
print(i)
print("---------------------------------------------------------")


# bisect를 이용한 구현
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
nums = [0,1,2,3,4,5,6,7,8,9]
n = 7
print(bisect_left(nums, n))
print(bisect_right(nums, n))
print(bisect_left(nums, 3))
print(bisect_right(nums, 3))
print(bisect(nums, n))
print("---------------------------------------------------------")

# bisect 응용 (특정 구간의 요소의 갯수 구하기)
nums = [-1, -3, 5, 5, 4, 7, 1, 7, 2, 5, 6]
nums.sort()  # 정렬은 필수

# 5 ~ 7 사이의 요소의 개수 구하기
print(nums)
print(bisect_left(nums, 5))
print(bisect_left(nums, 7))
print(abs(bisect_left(nums, 5) - bisect_left(nums, 7)))
print("---------------------------------------------------------")

# 5 ~ 7의 값을 가지는 요소의 개수 구하기
print(nums)
print(bisect_left(nums, 5), '왼쪽부터 5가 배치될 위치 이진 탐색')
print(bisect_right(nums, 7), '오른쪽부터 7이 배치될 위치 이진 탐색')
print(abs(bisect_right(nums, 7) - bisect_left(nums, 5)))

print("---------------------------------------------------------")
# nums 배열에 값 3을 삽입하기
insort(nums, 3)
print(nums)
