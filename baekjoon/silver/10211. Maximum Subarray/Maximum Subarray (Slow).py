# 10211. Maximum Subarray (실버 4)
# 알고리즘 분류 : 브루트포스, 누적 합

import sys
t = int(sys.stdin.readline())

for _ in range(t) :
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))

    total = sum(x)
    # i의 범위는 0 ~ n - 2
    # j의 범위는 1 ~ n
    for i in range(n - 2) :
        for j in range(i, n) :
            total = max(total, sum(x[i:j]))
    print(total)