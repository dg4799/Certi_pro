from bisect import bisect_left, bisect_right


a = [1,2,3,3,3,3,3,3,3,4,4,8,8,9]

# 값3의 왼쪽부터의 인덱스
print(bisect_left(a, 3))
# 값3의 오른쪽부터의 인덱스
print(bisect_right(a, 3))

# 값2~값4를 포함한 범위의 인덱스 갯수
print(abs(bisect_left(a, 2)-bisect_right(a, 4)))

# 값2~값4 사이의 인덱스 갯수
print(abs(bisect_right(a, 2)-bisect_left(a, 4)))

print('---------------------------------------------------------')

N = 7
x = 2
arr = [1,1,2,2,2,2,3]
# 여기서 값이 x인 원소의 갯수 출력
bisect_arr = abs(bisect_left(arr, x)-bisect_right(arr, x))
print(bisect_arr)