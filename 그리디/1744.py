from sys import stdin
from queue import PriorityQueue
'''
골드4: 수 묶기
1. 1보다 큰 수, 1, 0, 음수 4가지 유형으로 나누어 저장한다.
2. 1보다 큰 수는 정렬하여 최대값부터 차례대로 곱한 후 더한다. 마지막 남은 수가 홀수일 때 그냥 더한다.
3. 음수의 집합을 정렬해 최솟값부터 차례대로 곱한 후 더한다. 원소의 개수가 홀수이고, 0이 있을 때
    1개 남은 음수를 0과 곱해 0으로 만든다.
4. 값을 더하고 숫자 1의 개수를 더한다.
'''
N = int(stdin.readline())
ppq = PriorityQueue()
mpq = PriorityQueue()
one_cnt, result = 0, 0

for _ in range(N):
    data = int(stdin.readline())

    if data > 1:
        ppq.put(data * -1)
    elif data == 1:
        one_cnt += 1
    elif data <= 0:
        mpq.put(data)

while ppq.qsize() > 1:
    a = ppq.get() * -1
    b = ppq.get() * -1
    result += a * b

if ppq.qsize() > 0:
    result += ppq.get() * -1

while mpq.qsize() > 1:
    a = mpq.get()
    b = mpq.get()
    result += a * b

if mpq.qsize() > 0:
    result += mpq.get()

result += one_cnt
print(result)