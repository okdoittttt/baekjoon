import sys
'''
골드5: 신기한 소수 찾기
tip:
1의 자리 중, [2, 3, 5, 7]만 소수이므로 가지치기 방식으로 제외한다.
[자릿수가 두 개인 현재 수 * 10 + a]를 계산하여 소수인지 판별한다.
소수라면 재귀 함수로 자릿수를 하나 증가시킨다. 단, a가 짝수인 경우를 가지치기 방식으로 제외한다.
'''

'''
슈도코드
N(자릿수)
for i 2~현재 수/2+1까지 반복:
    if 현재 수 % i == 0"
        return 소수가 아님
        
def DFS(num):
    if 자릿수 == N:
        현재 수 출력
    else
        for i in 1~9:
            if i를 뒤에 붙인 새로운 수가 홀수이면서 소수일 때:
                DFS(수 * 10 + a)
'''
sys.setrecursionlimit(10 ** 4)
N = int(sys.stdin.readline())


def isPrime(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False

    return True


def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i):    # 소수라면 자릿수를 더해 계속 탐색
                DFS(number * 10 + i)


for i in [2, 3, 5, 7]:
    DFS(i)
