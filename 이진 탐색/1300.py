import sys
'''
골드1: K번째 수
작은 수의 개수가 k - 1개인 중앙값이 정답.
1. N * N 이차원 배열을 만든다.
2. 이차원 배열을 일차원 배열로 변환한다.
3. 일차원 배열을 오름차순 정렬한다
4. 정렬된 배열에서 k번째 값을 출력한다. 
'''
N = int(input())
K = int(input())

start, end, result = 1, K, 0

while start <= end:
    midi = int((start + end) / 2)
    count = 0

    for i in range(1, N+1):
        count += min(int(midi / i), N)
    if count < K:
        start = midi + 1
    else:
        result = midi
        end = midi - 1

print(result)
