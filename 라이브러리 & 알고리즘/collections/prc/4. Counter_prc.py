from collections import Counter


list_a = [1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4]
list_counter = Counter(list_a)                          # 리스트를 카운터로 변환
print(list_counter)
list_counter_key = list_counter.keys()
print(list_counter_key)
list_counter_value = list_counter.values()
print(list_counter_value)

print(list_counter[1])                                  # 변환한 리스트에 1의 갯수를 바로 출력 가능.
print(list_counter[2])
print(list_counter[3])
print(list_counter[4])

print(list_a.count(1))
print(list_a.count(2))
print(list_a.count(3))
print(list_a.count(4))


