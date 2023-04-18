# 1654. 랜선 자르기 (실버 2)
# 알고리즘 분류 : 이분 탐색, 매개 변수 탐색

import sys

k, n = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]

start, end = 1, max(lan)

for i in 