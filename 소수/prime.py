N = 100


# 가장 대표적인 소수를 구하는 방법
def isPrime(a):
    if a < 2:
        return False

    for i in range(2, a):
        if (a%i == 0):
            return False
    return True


# 에라토스테네스의 체
def isPrime_eratosthenes(n):
    # N까지의 모든 수를 True로 초기화 (소수라고 가정)
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        # p가 소수라면 (아직 지워지지 않았다면)
        if (prime[p] == True):
            # p의 배수들을 모두 False로 설정 (소수가 아님)
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # 소수만 담을 리스트
    primes = []
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)

    return primes


# 일반적인 방식의 소수 출력
primes = []
for i in range(N+1):
    if isPrime(i):
        primes.append(i)

print(primes)
print(isPrime_eratosthenes(N))