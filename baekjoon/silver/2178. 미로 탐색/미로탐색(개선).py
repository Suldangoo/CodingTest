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

# 상하좌우 이동 방향을 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    # 상하좌우를 살펴 1인 칸의 번호를 넣어둘 리스트 초기화
    nowFloor = []

    for i in queue:
        x, y = divmod(i, m) # 행, 열 구하기

        # 상하좌우로 이동하며 방문하지 않은 1인 칸의 번호를 nowFloor에 추가
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if 0 <= nx < n and 0 <= ny < m and visited[nx * m + ny] == False and graph[nx][ny] == 1:
                nowFloor.append(nx * m + ny)
                visited[nowFloor[-1]] = True

    floor += 1 # 층수 1 증가
    queue = nowFloor # 큐에 nowFloor 덮어쓰기

    if n * m - 1 in nowFloor : # 만약 nowFloor 안에 목적지가 존재한다면
        break # 반복문 break

print(floor) # 현재 층 수 (지나온 칸) 출력
