"""
양쪽 끝에서 빠르게 삭제와 추가를 할 수 있는 리스트형 컨테이너

- 리스트에서 빼고 넣고 하는것을 deque로 바꾼 후 처리하면 훨씬 속도가 빠르다.

deque 의 시간복잡도 O(1)
list 의 시간복잡도 O(N)
"""

from collections import deque

a = [10, 20, 30, 40, 50]
d = deque(a)                        # 리스트를 deque로 변환
print(d)
print(dir(d))

d.append(100)                       # append
print(d)
d.appendleft(1000)                  # appendleft
print(d)
print(d.pop())                      # d의 마지막 값을 뺌
print(d.popleft())                  # d의 가장 왼쪽 값을 뺌
print(d)
