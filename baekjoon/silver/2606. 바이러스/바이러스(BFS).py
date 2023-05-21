# 2606. 바이러스 (실버 3)
# 알고리즘 분류 : DFS, BFS, 그래프 이론

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

computer = int(input()) # 컴퓨터의 갯수
link = int(input()) # 연결된 컴퓨터 관계들의 갯수

# 컴퓨터의 개수만큼 빈 리스트로 초기화
graph = [[] for _ in range(computer + 1)]

# 사용자 입력 받기
for i in range(link):
    a, b = map(int, input().split())
    # a번 컴퓨터엔 b가 연결되어있고, b번 컴퓨터엔 a가 연결되어있음을 추가
    graph[a].append(b)
    graph[b].append(a)

# 방문 체크 리스트를 모두 False로 컴퓨터 개수만큼 초기화
visited = [False] * (computer + 1)

# dfs 함수 실행
bfs(graph, 1, visited)
print(visited.count(True) - 1) # 1번 컴퓨터를 제외한 바이러스에 걸린 컴퓨터의 개수 출력