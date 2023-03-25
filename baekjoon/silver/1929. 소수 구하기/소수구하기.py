# 1929. �Ҽ� ���ϱ� (�ǹ� 3)
# �˰��� �з� : �����佺�׳׽��� ü, ����, ������

m, n = map(int, input().split())

# �����佺�׳׽��� ü �˰����� ����Ͽ� �Ҽ��� ����
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

# m �̻� n ������ �Ҽ��� ���
for i in range(m, n + 1):
    if is_prime[i]:
        print(i)