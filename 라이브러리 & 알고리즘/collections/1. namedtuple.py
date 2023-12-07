
"""

[ collections ]
dict, list, set, tuple에 대한 대안을 제공하는 특수 컨테이너 데이터형

namedtuple : 이름이 있는 tuple
deque : 양쪽 끝에 빠르게 추가와 삭제 가능
Chainmap : 여러개의 딕셔너리, 튜플 등을 묶을 수 있음
Counter : 어떤 객체를 분해해서 구성요소의 갯수를 세줌
OrderedDict : 딕셔너리는 순서가 없지만 순서를 기억할 필요가 있을때 사용
defaultdict : 딕셔너리를 사용할때 키값이 없으면 에러가 나오는데 키값이 없을때 디폴트값을 새로 생성해줌.
UsderDict, UserList, UserString : 상속받아서 커스터마이징해서 만듬
"""


"""
namedtuple
- 튜플처럼 사용
- 이름을 통해 데이터로 접근 가능
- 메모리 활용 최적화
"""
from collections import namedtuple

named_tuple = namedtuple('Point', ['x', 'y'])     # 'Point'라는 이름으로 튜플 x, y를 선언)

p = named_tuple(11, y=22)                         # namedtuple 'Point'에 x와 y값을 줌

print(p[0] + p[1])
print(dir(p))                                     # p의 기능중 x,y 가 들어감
print(p.x, p.y)                                   # namedtuple 'Point'에 값을 넣은 p에 인덱스 이름인 x와 y로 접근가능
print('----------------------------------------------')

# print(p[x])                                     # x를 배열 인덱스로 접근은 하지 못함.

h, k = (3, 5)
print(h, k)                                       # 튜플의 언팩킹
i, j = p
print(i, j)                                       # p를 튜플을 언팩킹 하듯이 언팩킹이 가능함
print('----------------------------------------------')

d = { 'x' : 100, 'y' : 200}
p = named_tuple(**d)                              # 딕셔너리 형태도 p에 이와 같은 형태로 담을 수 있음
print(p)
print(p._asdict())                                # 딕셔너리 형태로 출력 가능

print(p._fields)                                  # 딕셔너리 key만 출력 가능
print('----------------------------------------------')

re_p = p._replace(x = 1000)
print(re_p)                                       # 값 변경 기능
print(p)                                          # 본래 key가 변경된건 아님
print('----------------------------------------------')

print(p.index(100))                               # index로 value 값의 인덱스를 찾을 수 있음
print(p.count(200))                               # count로 value 값의 숫자를 카운트 할 수 있음


