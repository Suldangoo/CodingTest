# 2579. 계단 오르기 (실버 3)
# 알고리즘 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

n = int(input()) # 계단의 갯수
score = [] # 계단에 적힌 점수
dp = [[0, 0]] # dp 테이블

for _ in range(n) :
    score.append(int(input())) # 점수를 입력받아 리스트에 저장

# 하나의 dp 테이블이 두 개의 요소를 가짐
# [0]은 바로 직전의 게단을 밟고 이번 계단을 밟을 때의 점수
# [1]은 직전의 계단을 밟지 않고, 그 전 계단의 점수들 중 최고 점수를 밟을 때의 점수
dp.append([score[0], score[0]]) # 첫 번째 계단 점수 삽입
score.pop(0)

for i in score :
    dp.append([dp[-1][1] + i, max(dp[-2][0] + i, dp[-2][1] + i)])
              
print(max(dp[-1]))