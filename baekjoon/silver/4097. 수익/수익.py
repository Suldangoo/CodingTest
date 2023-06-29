# 4097. 수익 (실버 3)
# 알고리즘 분류 : 카데인 알고리즘, 다이나믹 프로그래밍

import sys

while(True) :
    N = int(sys.stdin.readline()) # 수익의 개수 입력

    if N == 0 : # 0 입력 시 종료
        break

    table = [] # DP 테이블
    for _ in range(N) : # 각 일에 해당하는 수익 추가
        table.append(int(sys.stdin.readline()))

    best = table[0] # 배열의 첫 번째 원소를 초기값으로 설정
    total = 0 # 누적된 부분 배열의 합을 저장하는 변수

    # 2중 for문을 돌며 모든 경우를 브루트포스로 확인할 수 있으나, 그럴 경우 시간 복잡도는 O(n^3)까지 올라갈 수 있음
    # 아래의 Kadane 알고리즘으로 시간 복잡도를 O(n) 까지 줄일 수 있음
    for i in range(N):
        # 현재 원소와 이전까지 누적된 합 total과의 합 중 더 큰 값을 선택하여 total에 저장
        total = max(table[i], total + table[i])

        # 현재까지 찾은 부분 배열 중 가장 큰 합을 저장하는 변수 best와 비교하여, 더 큰 값을 best에 저장
        best = max(best, total)

    print(best)