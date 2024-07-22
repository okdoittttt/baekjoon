import sys
'''
실버5: 수들의 합5

어떠한 자연수 N은, 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 당신은 어떤 자연수 N(1 ≤ N ≤ 10,000,000)에 대해서, 이 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 알고 싶어한다.
이때, 사용하는 자연수는 N이하여야 한다. 예를 들어, 15를 나타내는 방법은 15, 7+8, 4+5+6, 1+2+3+4+5의 4가지가 있다. 반면에 10을 나타내는 방법은 10, 
1+2+3+4의 2가지가 있다. N을 입력받아 가지수를 출력하는 프로그램을 작성하시오.

풀이
N의 최대값이 10,000,000으로 O(nlogn)의 시간 복잡도 알고리듬을 사용하면 시간을 초과하므로 O(N)의 시간 복잡도 알고리듬을 사용해야 한다. 이때 투 포인터를 사용할 수 있다.
시작 인덱스와 종료 인덱스를 지정하여 연속된 수를 표현한다.
'''

'''
슈도코드

n변수 저장
사용변수 초기화 (count, start_index, end_index, sum = 1)

while end_index != n:
    if sum == n: 경우의 수 증가, end_index 증가, sum값 변경 ==> 정답 케이스
    elif sum > n: sum값 변경, start_index 증가
    else: end_inex 증가, sum값 변경
    
count 출력
'''
N = int(input())

count, start_index, end_index, sum = 1, 1, 1, 1

while end_index != N:
    if sum == N:
        count += 1
        end_index += 1
        sum += end_index

    elif sum > N:
        sum -= start_index
        start_index += 1

    else:
        end_index += 1
        sum += end_index


print(count)