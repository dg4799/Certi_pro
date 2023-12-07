"""
컨테이너 자료형 (dict, list(deque 포함), tuple)을 합쳐서 메소드를 사용할 수 있음.
"""

from collections import ChainMap

oneDict = {'one':1, 'two':2, 'three':3}
twoDict = {'four':4}
chain = ChainMap(oneDict, twoDict)
print(chain)                                # 딕셔너리를 ChainMap으로 연결

print('one' in chain)                       # oneDict와 twoDict 모두 검색됨
print('four' in chain)
print('five' in chain)
print('----------------------------------------------')


print(chain.values())
print(chain.keys())
print(chain.items())

print(chain['four'])                        # dict key로 oneDict와 twoDict 모두 검색됨
print('----------------------------------------------')


print(chain.maps)                           # dict를 리스트로 반환
print(chain.maps[0])
print(chain.maps[1])
print('----------------------------------------------')



one = [1,2,3,4]
two = [5,6,7,8]
three = ChainMap(one,two)                   # list도 합치기 가능
print(three)
print(7 in three)
print('----------------------------------------------')


from collections import deque               # deque list도 합칠 수 있음
d_one = deque(one)
d_two = deque(two)
d_three = ChainMap(d_one, d_two)
print(d_three)
print(7 in d_three)
print('----------------------------------------------')


t_one = (1,2,3,4)                           # tuple도 합치기 가능
t_two = (5,6,7,8)
t_three = ChainMap(t_one,t_two)
print(t_three)
print(7 in three)
print('----------------------------------------------')

