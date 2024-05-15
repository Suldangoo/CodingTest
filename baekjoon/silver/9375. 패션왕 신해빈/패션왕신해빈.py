# 9375. 패션왕 신해빈 (실버 3)
# 알고리즘 분류 : 조합론, 자료 구조

import sys
input = sys.stdin.readline

C = int(input()) # 테스트케이스 횟수 입력

# 테스트케이스 횟수만큼 반복
for _ in range(C) :
    wears = dict() # 의상 종류 : 의상 이름 리스트의 딕셔너리
    n = int(input())

    # 의상 개수만큼 반복
    for _ in range(n) :
        wear, type = input().split()
        # 해당 의상 종류가 이미 있다면 추가, 없다면 새로 생성
        if type in wears :
            wears[type].append(wear)
        else :
            wears[type] = [wear] # 반드시 리스트 형태로 넣어야 여러 옷을 추가 가능

    answer = 1 # 정답 조합을 곱할 것이기 때문에 1로 초기화

    # 조합식 : 모든 의상 카테고리의 수를 곱하여 최종 조합수 출력
    for i in wears :
        answer *= len(wears[i]) + 1 # 해당 의상 종류를 안 입은 것도 의상이기 때문에 +1

    # 모든 옷을 입지 않은 상황을 제외하고 출력, -1
    print(answer - 1)