from sys import stdin
'''
실버1: 회의실 배정
1. 회의 시작시간을 먼저 저장하는 것 보다 끝나는 시간을 저장하는 것이 유리하다.
2. schedule[][]에 값을 하나 선택하여 저장한 후, 해당 값과 비교하면서 회의실이 비어 있는지
    확인 한다.

'''
N = int(stdin.readline())
schedule = [[0] * 2 for _ in range(N)]
cnt = 0

for i in range(N):
    start, end = map(int, stdin.readline().split())

    schedule[i][0] = end
    schedule[i][1] = start

schedule.sort()
# print(schedule)
end = -1
for i in range(N):
    if schedule[i][1] >= end:
        end = schedule[i][0]
        cnt += 1

print(cnt)
