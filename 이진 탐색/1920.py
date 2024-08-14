import sys
'''
실버 4: 원하는 정수 찾기
: N의 최대 범위가 10**5 이므로 반복문으로 문제를 해결할 수 없다.
이진 탐색을 적용하면 O(nlogn)시간 복잡도로 해결할 수 있다.
'''
# 아래처럼 하면 시간 초과가 나온다.
'''
N = int(input())
li = list(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

for i in target:
    if i in li:
        print(1)
    else:
        print(0)
'''
N = int(input())
li = list(map(int, input().split()))
li.sort()

M = int(input())
_target = list(map(int, input().split()))

for i in range(M):
    flg = False
    start = 0
    end = len(li) - 1

    target = _target[i]

    while start <= end:
        mid = int((start + end) / 2)
        if li[mid] == target:
            flg = True
            break
        elif li[mid] > target:
            end = mid - 1
        elif li[mid] < target:
            start = mid + 1
        else:
            flg = True
            break

    if flg:
        print(1)
    else:
        print(0)
