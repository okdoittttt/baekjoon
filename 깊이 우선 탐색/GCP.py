# 최대공약수 계산(유클리드 호제법)
# 두 자연수 A, B에 대해 A를 B로 나눈 나머지가 R이라 할때,
# A와 B의 GCD는 B와 R의 GCD와 같다.
def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a%b)

print(GCD(192, 162))