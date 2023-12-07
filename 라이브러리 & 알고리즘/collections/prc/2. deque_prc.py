import time
from collections import deque


# [ deque ]
start = time.time()

d = deque([])
for i in range(10000000):
    d.append(i)
print(f'삽입 수행 시간, {time.time() - start} 초')

start = time.time()
for i in range(100):
    d.pop()
print(f'pop 수행 시간, {time.time() - start} 초')



# [ list ]
start = time.time()
list = []
for i in range(10000000):
    list.append(i)
print(f'삽입 수행 시간, {time.time() - start} 초')

start = time.time()
for i in range(100):
    list.pop(0)
print(f'pop 수행 시간, {time.time() - start} 초')



print('----------------------------------------------------------------')

# [ 리스트를 deque와 list로 수행 비교 ]

a = [i for i in range(10000000)]
d = deque(a)

start = time.time()
for i in range(100):
    d.pop()
print(f'deque pop 수행 시간, {time.time() - start} 초')

start = time.time()
for i in range(100):
    a.pop(0)
print(f'list pop 수행 시간, {time.time() - start} 초')
"""
리스트에서 빼고 넣고 하는것을 deque로 바꾼 후 처리하면 훨씬 속도가 빠르다.
"""
