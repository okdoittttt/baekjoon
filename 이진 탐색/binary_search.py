import sys
sys.setrecursionlimit(10 ** 4)
'''
이진 탐색에서 반복문, 재귀를 사용하는 시간 복잡도는 O(log n)이다.
이진 탐색은 정렬되어 있는 상탸에서만 사용할 수 있다.
재귀를 사용한 방식에는 함수 호출에서 오버헤드가 발생할 수 있다.
'''


# 반복문
def binary_search_while(_target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == _target:
            return mid

        elif data[mid] > _target:
            end = mid - 1

        else:
            start = mid + 1


# 재귀
def binary_search_recursion(_target, start, end, data):
    data.sort()
    if start > end:
        return -1

    mid = (start + end) // 2

    if data[mid] == _target:
        return mid

    elif data[mid] > _target:
        end = mid - 1

    else:
        start = mid + 1

    return binary_search_recursion(_target, start, end, data)


li = [3, 4, 1, 6, 8, 2, 5, 9, 10, 7]
target = 6
idx_recur = binary_search_recursion(target, 0, 10, li)
idx_while = binary_search_while(target, li)

print(idx_recur)
print(idx_while)