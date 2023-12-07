"""
- 리스트의 갯수를 빠르게 셀 수 있음

Counter의 시간복잡도 O(N)
list.count의 시간복잡도 O(N2)        # for문을 통해 count를 n번 하기 때문
"""

from collections import Counter

a = [1,1,1,2,3,4,5,5,5,6,6,7,8,8,9,10,10]
c = Counter(a)
print(c)                                      # 각 요소를 카운트하여 요약헤서 딕셔너리로 출력

for i in c:
    print(i, end=', ')                       # c의 요소를 요약해서 출력
print("")
print('----------------------------------------------')

for i in c.elements():
    print(i, end=', ')                       # c의 모든 요소를 출력
print("")
print('----------------------------------------------')

print(c.keys())                             # 딕셔너리 keys
print(c.values())                           # 딕셔너리 values
print(c.items())                            # 딕셔너리 items

print(c.most_common())                      # Cunter된 딕셔너리를 리스트안의 튜플로 바로 반환 가능
print('----------------------------------------------')


s = 'hello. world'
sc = Counter(s)
print(sc)                                   # String을 Counter하면 각각 문자열의 갯수를 요약하여 딕셔너리로 반환

sc.update('hello')
print(sc)                                   # sc에 hello를 추가하여 Counter

sc.subtract('hello')
print(sc)                                   # sc에 hello를 뺌
print('----------------------------------------------')


# 사용할일이 없는 딕셔너리 카운터
d = {'one':100, 'two':200, 'three':200}
s = Counter(d)
print(s)                                    # 딕셔너리를 Counter로 변환하면 value가 카운트 된것으로 출력됨

d = {'one':'100', 'two':'200', 'three':'200'}
s = Counter(d)
print(s)                                    # 딕셔너리를 Counter로 변환하면 value가 카운트 된것으로 출력됨
print('----------------------------------------------')
