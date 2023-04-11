# 2178. 미로 탐색 (실버 1)
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [False] * (n * m) # 열 * 행 크기의 False로 채워진 방문 체크 리스트

floor = 1 # 현재까지 지나온 칸 수, 층 수
queue = [0] # 상하좌우를 살펴볼 큐에 들어간 칸의 번호
visited[0] = True # 방문 체크 리스트

while True : 
    # 상하좌우를 살펴 1인 칸의 번호를 넣어둘 리스트 초기화
    nowFloor = []

    for i in queue :
        a = i // m # 번호를 받았을 때 열 결정
        b = i % m # 번호를 받았을 때 행 결정

        # 상하좌우를 각각 살펴보고 1이라면 nowFloor에 추가
        # 조건 1. 상하좌우를 봤을 때 범위를 벗어나면 실행하지 않음
        # 조건 2. 상하좌우를 봤을 때 해당 칸이 방문 체크가 되어있다면 실행하지 않음
        # 조건 3. 상하좌우를 봤을 때 해당 칸이 1이어야 함
        if a - 1 >= 0 and visited[(a - 1) * m + b] == False and graph[a - 1][b] == 1 :
            nowFloor.append((a - 1) * m + b)
            visited[nowFloor[-1]] = True
        if a + 1 < n and visited[(a + 1) * m + b] == False and graph[a + 1][b] == 1 :
            nowFloor.append((a + 1) * m + b)
            visited[nowFloor[-1]] = True
        if b - 1 >= 0 and visited[a * m + b - 1] == False and graph[a][b - 1] == 1 :
            nowFloor.append(a * m + b - 1)
            visited[nowFloor[-1]] = True
        if b + 1 < m and visited[a * m + b + 1] == False and graph[a][b + 1] == 1 :
            nowFloor.append(a * m + b + 1)
            visited[nowFloor[-1]] = True

    floor += 1 # 층수 1 증가
    queue = nowFloor # 큐에 nowFloor 덮어쓰기

    if n * m - 1 in nowFloor : # 만약 nowFloor 안에 목적지가 존재한다면
        break # 반복문 break

print(floor) # 현재 층 수 (지나온 칸) 출력