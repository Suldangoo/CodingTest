# 14501. 퇴사 (실버 3)
# 알고리즘 분류 : 다이나믹 프로그래밍, 브루트 포스, 냅색

import sys

n = int(sys.stdin.readline()) # 상담 일 수
t = [] # 각 상담에 소요되는 일수
p = [] # 각 상담에 대한 보수
dp = [0] * (n + 1) # 각 날짜별 최대 수익

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    t.append(x)
    p.append(y)

# 역순으로 dp 계산
for i in range(n - 1, -1, -1):
    if i + t[i] > n: # 상담 기간이 퇴사일을 초과하는 경우
        dp[i] = dp[i + 1] # 이전 최대 수익으로 대체
    else:
        dp[i] = max(dp[i + 1], dp[i + t[i]] + p[i]) # 이전 최대 수익과 새로운 수익 + 해당 상담 후 일의 수익 중 큰 값 선택

print(dp[0]) # 최종 최대 수익 출력