# 1966. 한수 (실버 3)
# 알고리즘 분류 : 자료구조, 큐, 구현, 시뮬레이션

import sys
from collections import deque

test = int(sys.stdin.readline())

for _ in range(test) :
    n, m = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))

    queue = deque(importance) # 중요도를 그대로 살려 큐 생성
    importance.sort() # 중요도를 오름차순으로 정렬

    i = 1 # 지금 출력한 종이가 몇 번째로 출력한 종이인지 체크할 변수
    # 리스트의 길이가 0이 될 때까지 반복
    while(len(importance) > 0) :
        if queue[0] == importance[-1] : # 만약 지금 제일 앞에 있는 종이가 가장 중요도가 높을 경우
            del importance[-1] # 가장 높은 중요도 리스트 하나 제거
            queue.popleft() # 종이 출력
            if m == 0 : # 만약 이번 종이가 추적중인 종이었다면
                print(i) # i 출력 후 break
                break
            else : # 추적중인 종이가 아니라면
                i += 1 # 출력한 종이 갯수 증가
                m -= 1 # 현재 추적중인 종이 순서 갱신
        else :
            queue.append(queue.popleft()) # 중요도가 더 높은게 있다면 가장 뒤로 빼버리기
            if (m == 0) : # 그 종이가 추적중인 종이었다면
                m = len(importance) - 1 # 가장 뒤로 보내버리기
            else :
                m -= 1 # 아니라면 추적중인 종이 순서 갱신