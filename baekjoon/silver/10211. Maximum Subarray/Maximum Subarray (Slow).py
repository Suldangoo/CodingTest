# 10211. Maximum Subarray (�ǹ� 4)
# �˰��� �з� : ���Ʈ����, ���� ��

import sys
t = int(sys.stdin.readline())

for _ in range(t) :
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))

    total = sum(x)
    # i�� ������ 0 ~ n - 2
    # j�� ������ 1 ~ n
    for i in range(n - 2) :
        for j in range(i, n) :
            total = max(total, sum(x[i:j]))
    print(total)