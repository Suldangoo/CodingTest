# 2178. 미로 탐색 (실버 1)
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque

def bfs(graph, start, visited) :
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

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n * m + 1)]
numList = []
visited = [False] * (n * m + 1)

for _ in range(n) :
    numList.append(sys.stdin.readline())

for i in range(n) :
    for j in range(m - 1) :
        if numList[i][j] + numList[i][j + 1] == 2 :
            graph[i * m + j + 1].append(i * m + j + 2)
            graph[i * m + j + 2].append(i * m + j + 1)

for i in range(m) :
    for j in range(n - 1) :
        if numList[j][i] + numList[j + 1][i] == 2 :
            graph[i * m + j + 1].append((i + 1) * m + j)
            graph[(i + 1) * m + j].append(i * m + j + 1)

print(bfs(graph, 1, visited))