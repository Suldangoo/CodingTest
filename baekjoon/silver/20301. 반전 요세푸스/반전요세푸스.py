# 20301. 반전 요세푸스 (실버 3)
# 알고리즘 분류 : 구현, 자료 구조, 시뮬레이션, 덱

import sys
input = sys.stdin.readline

# N명의 사람들 중 K번째 사람을 순서대로 제거하며, M명 제거되면 방향이 반전
N, K, M = map(int, input().split())

nums = [i for i in range(1, N + 1)] # 1번부터 시작하는 번호 리스트

start = 0 # 시작 포인터
count = 0 # 몇 번 빠졌는지 체크

while nums :
    end = (start + K - 1) % len(nums) # 오른쪽으로 K번 돌며 nums의 길이를 넘지 않도록 포인터 갱신
    print(nums.pop(end)) # 포인터에 해당하는 사람 pop

    count += 1 # 한 명 빠짐을 체크

    # 만약 사람이 M번 빠졌다면, 방향을 오른쪽 ↔ 왼쪽 반전
    # 방향을 반전한다는 것은, 리스트의 순서가 반전된다는 것과 마찬가지
    if count == M :
        nums.reverse() # 리스트 순서를 반전
        end = len(nums) - end # 포인터 위치 반전
        count = 0
    
    start = end # 시작점을 갱신