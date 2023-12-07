"""
딕셔너리는 key와 value가 모두 있어야 생성할 수 있는데
defalutdict는 value의 type만 넣어서 key만으로 딕셔너리를 선언할 수 있음.

리스트로 하나씩 변수를 만들어서 저장하는건 O(변수 개수)
딕셔너리 하나로 만들어서 저장하는건 O(1)
"""

# test_d = {'one':1, 'two':2. 출근길 라디오, 'three'}  # 이렇게 value가 없이 딕셔너리 선언을 하지 못함

from collections import defaultdict
d = defaultdict(str)                    # value값의 type을 defaultdict에 넣어 만들어주고
d['one'] = '1'                          # key와 value를 입력하면
d['two'] = '2. 출근길 라디오'
d['three'] = '3'
print(d)                                # 딕셔너리가 만들어짐

d = defaultdict(list)                   # 이때 list로 만들어서
d['one'] = '1'
d['two'] = '2. 출근길 라디오'
d['three']                              # value가 없는 key에 list []가 초기값으로 들어감
print(d)


d = defaultdict(int)                      # 이때 list로 만들어서
d['one'] = 1
d['two'] = 2
d['three']                              # value가 없는 key에 0이 초기값으로 들어감
print(d)


print('----------------------------------------------------------')
print(dir(d))                           # 딕셔너리의 메소드가 모두 들어있음.

d = defaultdict(int)
for i in range(10):
    d[i] = 1                            # 딕셔너리를 1로 모두 초기화해서 생성 가능.
print(d)

