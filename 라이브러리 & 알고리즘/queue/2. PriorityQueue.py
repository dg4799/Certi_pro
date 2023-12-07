"""
우선순위큐(PriorityQueue)는 우선순위에 따라 가장 우선순위가 높은 데이터를 가장 먼저 삭제하는 자료구조
- 큐(queue) 가장 먼저 넣은 데이터를 가장 먼저 삭제하는 자료구조
- 스택(Stack) 가장 먼저 넣은 데이터를 가장 나중에 삭제하는 자료구조

★★★★★ heap과 같은 성질을 가짐
- heap과 같이 완전 이진트리 구조 : 가장 상단의 값이 가장 작은 값임, 왼쪽 자식노드와 오른쪽 자식노드 보다 작은수가 상단(부모노드)에 위치함
"""


from queue import PriorityQueue

q = PriorityQueue()
q.put(3)
q.put(4)
q.put(1)
q.put(6)

print(q.get())
print(q.get())
print(q.get())
print(q.get())
"""
get을 통해 가장 상단(가장 작은)값을 뽑을 수 있음
"""
print("--------------------------------------------------------")

q.put(-3)
q.put(-4)
q.put(-1)
q.put(-6)

print(-q.get())
print(-q.get())
print(-q.get())
print(-q.get())
"""
put할때 마이너스를 넣고 get할때 마이너스로 부호를 바꿔주면 가장 큰 숫자의 순서로 출력됨
"""
