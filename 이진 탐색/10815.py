import sys
'''
실버5: 숫자카드
'''
N = int(input())
li = list(map(int, input().split()))
li.sort()

M = int(input())
_target = list(map(int, input().split()))


for i in range(M):
    start = 0
    end = N - 1

    target = _target[i]
    flg = False

    while start <= end:
        midi = int((start + end) / 2)

        if li[midi] == target:
            flg = True
            break
        elif li[midi] > target:
            end = midi - 1
        elif li[midi] < target:
            start = midi + 1
        else:
            flg = True
            break

    print(1 if flg else 0, end=' ')