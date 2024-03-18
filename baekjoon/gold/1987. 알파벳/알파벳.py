# 1987. 알파벳 (실버 4)
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 백트래킹, 깊이 우선 탐색

import sys
input = sys.stdin.readline

# dfs 재귀 함수 (x축, y축 위치정보, 그래프, 이동 횟수, 보유 사과)
def dfs(x, y, graph, alpha) :
    # 4방향으로 이동하며 재귀
    for i in range(4) :
        ddx = x + dx[i]
        ddy = y + dy[i]

        # 이동 후 범위를 벗어났다면 패스
        if ddx < 0 or ddx > r or ddy < 0 or ddy > c :
            continue

        # 이동한 장소의 알파벳이 이미 보유중이라면 패스
        if graph[ddx][ddy] in alpha :
            continue

        # 이동한 곳이 벽이라면 (-1) 패스
        if graph[ddx][ddy] == 1 :
            apple += 1
            isFind = True
        else :
            isFind = False

        tmp = graph[x][y] # 기존 값 저장
        graph[x][y] = -1 # 지나간 길은 벽인 -1로 채우기
        dfs(ddx, ddy, graph, count + 1, apple)
        graph[x][y] = tmp # 재귀했다면 기존 값 복원
        if isFind : # 얻은 사과가 있다면 반납
            apple -= 1
    return

graph = [] # 그래프
r, c = map(int, input().split())
for i in range(r) :
    graph.append(input())

answer = 0 # 정답
alpha = [] # 보유한 알파벳 리스트

# 위치 정보 변수
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

dfs(r, c, graph, alpha) # 탐색

print(alpha)