# 11724. 연결 요소의 개수 (실버 2)
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

n, m = map(int, input().split()) # 정점의 개수 n과 간선의 개수 m
graph = [[] for _ in range(n + 1)] # 정점의 개수 + 1 만큼의 노드 생성
visited = [False] * (n + 1) # 방문 체크 리스트
connect = 0 # 연결 요소의 개수

for _ in range(m) :
    u, v = map(int, input().split()) # 두 정점의 번호 입력
    # 각 정점에 연결 노드 번호 추가
    graph[u].append(v)
    graph[v].append(u)

# 1번 노드부터 시작하여 탐색하고 온 뒤 연결요소 개수 증가
for i in range(1, n + 1) :
    # 방문하지 않았다면
    if not visited[i] :
        bfs(graph, i, visited) # bfs로 쭉 탐색
        connect += 1 # 연결요소 1 증가

print(connect) # 총 연결 요소 출력