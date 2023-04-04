# 10211. Maximum Subarray (실버 4)
# 알고리즘 분류 : 카데인 알고리즘, 브루트포스, 누적 합

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))

    best = x[0]   # 배열의 첫 번째 원소를 초기값으로 설정
    total = 0     # 누적된 부분 배열의 합을 저장하는 변수

    # 2중 for문을 돌며 모든 경우를 브루트포스로 확인할 수 있으나, 그럴 경우 시간 복잡도는 O(n^3)까지 올라갈 수 있음
    # 아래의 Kadane 알고리즘으로 시간 복잡도를 O(n) 까지 줄일 수 있음
    for i in range(n):
        # 현재 원소와 이전까지 누적된 합 total과의 합 중 더 큰 값을 선택하여 total에 저장
        total = max(x[i], total + x[i])

        # 현재까지 찾은 부분 배열 중 가장 큰 합을 저장하는 변수 best와 비교하여, 더 큰 값을 best에 저장
        best = max(best, total)

    print(best)