# 11866. 요세푸스 문제 0 (실버 5)
# 알고리즘 분류 : 구현, 자료 구조, 큐

import sys
n, k = map(int, sys.stdin.readline().split())

nums = [i for i in range(1, n + 1)]
m = 0

print('<', end = '')

while nums :
    nums.append(nums.pop(0))
    m += 1

    if m == k - 1 :
        print(nums.pop(0), end = '')
        m = 0
        if nums :
            print(', ', end = '')

print('>')