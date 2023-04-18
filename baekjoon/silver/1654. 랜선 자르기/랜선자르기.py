# 1654. 랜선 자르기 (실버 2)
# 알고리즘 분류 : 이분 탐색, 매개 변수 탐색

import sys

k, n = map(int, sys.stdin.readline().split()) # 랜선의 개수와 목표 개수를 입력받음
lan = [int(sys.stdin.readline()) for _ in range(k)] # 랜선들을 입력받음

# 최소 길이를 1, 최대 길이를 랜선의 가장 긴 길이로 설정
start, end = 1, max(lan)

# 이분 탐색이 아예 종료될 때까지 돌린다
while start <= end :
    mid = (start + end) // 2
    lans = 0

    # 현재 mid의 길이로 랜선이 몇 개나 나오는지 확인
    for i in lan :
        lans += i // mid

    if lans >= n : # 만약 랜선이 목표치보다 더 많이 나온다면, 좀 더 길게 잘라보기
        start = mid + 1
    else : # 만약 랜선이 목표치보다 더 적게 나온다면, 길이를 줄여보기
        end = mid - 1

print(end)