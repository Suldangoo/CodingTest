# 2178. 미로 탐색 (실버 1)
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [False] * (n * m)

def bfs(start) :
    cnt = 0
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        cnt += 1
        for i in graph[v] :
            if int(i) == n * m :
                return cnt
            elif not visited[i] :
                queue.append(i)
                visited[i] = True

