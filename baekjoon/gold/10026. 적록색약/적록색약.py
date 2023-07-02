# 10026. 적록색약 (골드 5)
# 알고리즘 분류 : 그래프 이론, 그래프 탐색

# deque를 이용한 BFS로 풀이
from collections import deque

def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

N = int(input())
table1 = [] # 적록색약이 아닌 정상적인 색판
table2 = [] # 적록색약이 보는 두 색의 색판

for _ in range(N) :
    temp = input()
    color = []

    for i in temp :
        color.append(i)
    table1.append(color)
    color = []

    for i in temp :
        if i == 'G' : # 적록색약은 G를 R로 대체
            color.append('R')
        else :
            color.append(i)
    table2.append(color)

width = len(table1[0])
graph1 = graph2 = [[] for _ in range(width * N)] # 정점의 개수만큼의 노드 생성
visited1 = visited2 = [False] * (width * N) # 방문 체크 리스트
color1 = color2 = 0 # 연결 요소의 개수

for i in N :
    for j in range(width - 1) :
        if table1[i][j] == table1[i][j + 1] :
            graph1[i * width + j] = i * width + j + 1
            graph1[i * width + j + 1] = i * width + j

        if table2[i][j] == table2[i][j + 1] :
            graph2[i * width + j] = i * width + j + 1
            graph2[i * width + j + 1] = i * width + j

