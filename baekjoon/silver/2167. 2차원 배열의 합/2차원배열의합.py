# 2167. 2차원 배열의 합 (실버 5)
# 알고리즘 분류 : 구현, 누적 합

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
nums = []
part_sum = [[0]*(m+1) for _ in range(n+1)] # 2차원 배열의 부분 합을 저장할 배열

for i in range(n):
    nums.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(m):
        # 2차원 배열의 부분 합을 누적하여 저장
        part_sum[i+1][j+1] = nums[i][j] + part_sum[i][j+1] + part_sum[i+1][j] - part_sum[i][j]

k = int(sys.stdin.readline())

for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().rstrip().split())
    # 중복 계산을 피하기 위해 저장된 부분 합을 이용하여 구함
    print(part_sum[x][y] - part_sum[x][j-1] - part_sum[i-1][y] + part_sum[i-1][j-1])