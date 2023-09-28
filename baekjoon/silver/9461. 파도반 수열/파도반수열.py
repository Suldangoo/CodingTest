# 9461. 파도반 수열 (실버 3)
# 알고리즘 분류 : 수학, 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

# 두 삼각형의 빗변에 해당하지 않는 삼각형들
padovan = [1, 1, 1, 2, 2]

# 두 삼각형의 빗변이 한 변이 되는 삼각형의 규칙
# 가장 마지막 삼각형의 한 변 + 네 번 전의 삼각형의 한 변

# 이미 5개는 채워놨으므로, 100개까지 채우기
for _ in range(95) :
    padovan.append(padovan[-1] + padovan[-5])

for _ in range(int(input())) :
    # 입력한 숫자 -1번 번지의 리스트 출력
    print(padovan[int(input()) - 1])