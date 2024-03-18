# 26170. 사과 빨리 먹기 (실버 2)
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 백트래킹, 깊이 우선 탐색

import sys
input = sys.stdin.readline

answer = [] # 정답들이 담긴 리스트

# 위치 정보 변수
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# dfs 재귀 함수 (x축, y축 위치정보, 그래프, 이동 횟수, 보유 사과)
def dfs(x, y, graph, count, apple) :
    # 보유한 사과가 세 개가 되었다면 정답 리스트에 이동 횟수 추가
    if apple == 3 :
        answer.append(count)
        return

    # 4방향으로 이동하며 재귀
    for i in range(4) :
        ddx = x + dx[i]
        ddy = y + dy[i]

        # 이동 후 범위를 벗어났다면 패스
        if ddx < 0 or ddx > 4 or ddy < 0 or ddy > 4 :
            continue

        # 이동한 곳이 벽이라면 (-1) 패스
        if graph[ddx][ddy] == -1 :
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
for i in range(5) :
    graph.append(list(map(int, input().split())))
r, c = map(int, input().split())

apple = 0 # 사과의 개수
if graph[r][c] == 1 : # 시작 위치에 사과가 있다면 사과 1개 추가
    apple += 1

dfs(r, c, graph, 0, apple) # 탐색

if len(answer) == 0 :
    print(-1) # 정답 리스트가 비었다면 -1 출력
else :
    print(min(answer)) # 정답이 하나라도 있다면 최솟값 출력