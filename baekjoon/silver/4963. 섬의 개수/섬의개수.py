# 4963. 섬의 개수 (실버 2)
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 너비 우선 탐색

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 위치 정보 변수 (가로 세로 대각선)
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def dfs(y, x) :
    if x < 0 or x >= w or y < 0 or y >= h :
        return False
        
    if graph[y][x] == 1:
        graph[y][x] = 0

        for i in range(8) :
            ddx = x + dx[i]
            ddy = y + dy[i]

            dfs(ddy, ddx)
        return True
    return False

while True :
    w, h = map(int, input().split())

    if w == h == 0 :
        break

    graph = []
    for _ in range(h) :
        graph.append(list(map(int, input().split())))

    result = 0

    for i in range(h) :
        for j in range(w) : 
            if dfs(i, j) == True :
                result += 1

    print(result)