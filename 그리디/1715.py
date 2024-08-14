from sys import stdin
from queue import PriorityQueue
'''
골드4: 카드 정렬하기
우선순위 큐: 제거될 때는 가장 작은 값을 제거
'''
N = int(stdin.readline())
pq = PriorityQueue()

for _ in range(N):
    pq.put(int(stdin.readline()))

result = 0
a, b = 0, 0
while pq.qsize() > 1:
    a = pq.get()
    b = pq.get()
    tmp = a + b
    result += tmp

    pq.put(tmp)

print(result)
