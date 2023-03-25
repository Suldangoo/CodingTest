# 1929. 소수 구하기 (실버 3)
# 알고리즘 분류 : 에라토스테네스의 체, 수학, 정수론

m, n = map(int, input().split())

# 에라토스테네스의 체 알고리즘을 사용하여 소수를 구함
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

# m 이상 n 이하의 소수를 출력
for i in range(m, n + 1):
    if is_prime[i]:
        print(i)