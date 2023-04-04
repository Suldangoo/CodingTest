# 1260. DFS와 BFS (실버 2)
# 알고리즘 분류 : DFS, BFS, 그래프 이론, 그래프 탐색

# 필요한 라이브러리 임포트
import sys
from collections import deque

# DFS 함수 정의, 필요한 인자는 그래프, 시작노드 번호, 방문체크 리스트
def dfs(graph, n, visited) :
    visited[n] = True
    print(n, end = " ")
    for i in graph[n] :
        if not visited[i] :
            dfs(graph, i, visited) # 재귀함수로 풀이

# BFS 함수 정의, 필요한 인자는 그래프, 시작노드 번호, 방문체크 리스트
def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft() # 큐로 풀이
        print(v, end = " ")
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

# 노드의 개수, 간선의 개수, 시작 번호를 입력받음
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)] # 빈 그래프 초기화

# 노드의 번호가 작은 노드부터 탐색해야 하므로, 입력을 곧이곧대로 넣으면 정렬되지 않음
# 따라서 2, 1이라면 1, 2처럼 오름차순으로 바꿔주고, 다 입력받은 후 정렬해줘야함
edges = []
for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a
    edges.append((a, b)) # 튜플 형태로 append
edges.sort()

# 정렬 된 입력값들을 그래프에 삽입
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

# 방문체크 리스트 초기화 후 dfs함수 실행
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()

# 방문체크 리스트 초기화 후 bfs함수 실행
visited = [False] * (n + 1)
bfs(graph, v, visited)