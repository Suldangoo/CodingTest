# 18429. 근손실 (실버 2)
# 알고리즘 분류 : 브루트포스 알고리즘, 백트래킹

from itertools import permutations
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(permutations(range(N), N))
kit = list(map(int, sys.stdin.readline().split()))
result = 0

for i in arr :
    weight = 500
    for j in i :
        weight += kit[j] - K
        if weight < 500 :
            result -= 1
            break
    result += 1

print(result)