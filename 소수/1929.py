import math
'''
실버3: 소수 구하기
일반적인 소수를 구하는 방식은 시간 제한에 걸린다.
아레토스테네스의 체를 이용하여 풀어야 한다.
'''
M, N = map(int, input().split())
A = [0] * (N+1)

# 인덱스의 값으로 리스트 초기화
for i in range(2, N+1):
    A[i] = i

for i in range(2, int(math.sqrt(N)) + 1):
    if A[i] == 0:
        continue
    for j in range(i+i, N+1, i):
        A[j] = 0

for i in range(M, N+1):
    if A[i] != 0:
        print(A[i])
