# 1987. 알파벳 (골드 4)
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 백트래킹, 깊이 우선 탐색

import sys
input = sys.stdin.readline

# dfs 재귀 함수 (x축, y축 위치정보, 그래프, 이동 횟수, 보유 사과)
def dfs(x, y, graph, alpha, count) :
    global answer  # 전역 변수로 설정

    # 현재 위치의 알파벳을 방문했다고 표시
    alpha[ord(graph[x][y]) - ord('A')] = True

    # 4방향으로 이동하며 재귀
    for i in range(4) :
        ddx = x + dx[i]
        ddy = y + dy[i]

        # 이동 후 범위를 벗어났다면 패스
        if ddx < 0 or ddx >= r or ddy < 0 or ddy >= c :
            continue

        # 이동한 장소의 알파벳이 이미 보유중이라면 패스
        if alpha[ord(graph[ddx][ddy]) - ord('A')] :
            continue

        dfs(ddx, ddy, graph, alpha, count + 1) # 다음 dfs 시작
    
    # 현재 위치에서의 탐색이 종료되면, 최대 길이를 갱신
    answer = max(answer, count)

    # 현재 위치의 알파벳을 다시 방문하지 않은 것으로 표시
    alpha[ord(graph[x][y]) - ord('A')] = False

answer = 0 # 최대 길이
graph = [] # 그래프
r, c = map(int, input().split())
for i in range(r) :
    graph.append(input().rstrip())

# 알파벳 방문 여부를 체크하기 위한 리스트
alpha = [False] * 26

# 위치 정보 변수
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

dfs(0, 0, graph, alpha, 1) # 탐색

print(answer)