# 2167. 2차원 배열의 합 (실버 5)
# 알고리즘 분류 : 구현, 누적 합

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
nums = []

for _ in range(n) :
    nums.append(list(map(int, sys.stdin.readline().rstrip().split())))

k = int(sys.stdin.readline())

for _ in range(k) :
    i, j, x, y = map(int, sys.stdin.readline().rstrip().split())
    sum = 0
    for a in range(i, x + 1) :
        for b in range(j, y + 1) :
            sum += nums[a - 1][b - 1]

    print(sum)