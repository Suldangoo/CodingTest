# 1205. 등수 구하기 (실버 4)
# 알고리즘 분류 : 구현, 이진 탐색

import sys
input = sys.stdin.readline

N, score, P = map(int, input().split())

if N > 0 :
    ranking = list(map(int, input().split()))
else : # 만약 등록된 랭킹이 하나도 없다면, 1등으로 마무리
    print(1)
    exit(0)

result = 1 # 이론상 최대 점수

for i in range(N) : # 0부터 N - 1까지 반복
    if score > ranking[i] : # 점수가 랭킹의 점수보다 크다면, 마무리
        break
    elif score < ranking[i] : # 점수가 랭킹의 점수보다 작다면
        if i == N - 1: # 리스트의 끝일 때
            if N < P : # 뒤에 빈자리가 있다면 등수 올리고 마무리
                result += 1
            else : # 뒤에 빈자리가 없다면 -1로 마무리
                result = -1
                break
        else : # 리스트의 끝이 아니라면, 등수를 올리고 다음 점수 확인
            result += 1
            continue
    else : # 점수가 랭킹의 점수와 동일하다면
        if i == N - 1: # 리스트의 끝일 때
            if N < P : # 뒤에 빈자리가 있다면 현재 점수로 마무리
                break
            else : # 뒤에 빈자리가 없다면 -1로 마무리
                result = -1
                break
        else : # 리스트의 끝이 아니라면 이어서 다음 점수를 확인
            continue

print(result)