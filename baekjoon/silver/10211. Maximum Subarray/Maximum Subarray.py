# 10211. Maximum Subarray (�ǹ� 4)
# �˰��� �з� : ī���� �˰���, ���Ʈ����, ���� ��

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))

    best = x[0]   # �迭�� ù ��° ���Ҹ� �ʱⰪ���� ����
    total = 0     # ������ �κ� �迭�� ���� �����ϴ� ����

    # 2�� for���� ���� ��� ��츦 ���Ʈ������ Ȯ���� �� ������, �׷� ��� �ð� ���⵵�� O(n^3)���� �ö� �� ����
    # �Ʒ��� Kadane �˰������� �ð� ���⵵�� O(n) ���� ���� �� ����
    for i in range(n):
        # ���� ���ҿ� �������� ������ �� total���� �� �� �� ū ���� �����Ͽ� total�� ����
        total = max(x[i], total + x[i])

        # ������� ã�� �κ� �迭 �� ���� ū ���� �����ϴ� ���� best�� ���Ͽ�, �� ū ���� best�� ����
        best = max(best, total)

    print(best)