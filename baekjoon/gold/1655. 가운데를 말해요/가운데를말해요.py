# 1655. 가운데를 말해요 (골드2)
# 알고리즘 분류 : 우선순위 큐, 힙, 자료구조

import heapq # 힙큐 모듈 사용
import sys

# 입력받기
n = int(sys.stdin.readline().strip())
nums = []

# 중앙값 기준으로 작은 값들을 max_heap에, 큰 값들은 min_heap에 저장
max_heap = [] # 최대 힙
min_heap = [] # 최소 힙

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    # 짝수 번째 수인 경우
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num)) # 최대 힙에 저장
    # 홀수 번째 수인 경우
    else:
        heapq.heappush(min_heap, (num, num)) # 최소 힙에 저장

    # 최대 힙의 최댓값이 최소 힙의 최솟값보다 클 경우 두 값을 교환
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-min_value, min_value))
        heapq.heappush(min_heap, (max_value, max_value))
    
    # 중앙값 출력
    print(max_heap[0][1])