"""
Queue

리스트의 인자를 넣어 연산하는것 시간복잡도 O(N)
 - 리스트의 첫번째, 두번째, 세번째 넣은 것을 찾으려고 연산하려면 리스트를 길이만큼 탐색해서 뽑아냄

Queue는 시간복잡도 O(1)
"""
from queue import Queue

que = Queue()                   # Queue를 만들어서 put으로 인자를 넣음
que.put(4)
que.put(5)
que.put(6)

print(que.get())                # get으로 인자를 출력하면 가장 먼저 들어간 인자가 출력됨
print(que.get())
print(que.get())
