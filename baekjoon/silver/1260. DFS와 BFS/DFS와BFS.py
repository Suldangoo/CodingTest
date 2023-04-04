# 1260. DFS�� BFS (�ǹ� 2)
# �˰��� �з� : DFS, BFS, �׷��� �̷�, �׷��� Ž��

# �ʿ��� ���̺귯�� ����Ʈ
import sys
from collections import deque

# DFS �Լ� ����, �ʿ��� ���ڴ� �׷���, ���۳�� ��ȣ, �湮üũ ����Ʈ
def dfs(graph, n, visited) :
    visited[n] = True
    print(n, end = " ")
    for i in graph[n] :
        if not visited[i] :
            dfs(graph, i, visited) # ����Լ��� Ǯ��

# BFS �Լ� ����, �ʿ��� ���ڴ� �׷���, ���۳�� ��ȣ, �湮üũ ����Ʈ
def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft() # ť�� Ǯ��
        print(v, end = " ")
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

# ����� ����, ������ ����, ���� ��ȣ�� �Է¹���
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)] # �� �׷��� �ʱ�ȭ

# ����� ��ȣ�� ���� ������ Ž���ؾ� �ϹǷ�, �Է��� ���̰��� ������ ���ĵ��� ����
# ���� 2, 1�̶�� 1, 2ó�� ������������ �ٲ��ְ�, �� �Է¹��� �� �����������
edges = []
for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a
    edges.append((a, b)) # Ʃ�� ���·� append
edges.sort()

# ���� �� �Է°����� �׷����� ����
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

# �湮üũ ����Ʈ �ʱ�ȭ �� dfs�Լ� ����
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()

# �湮üũ ����Ʈ �ʱ�ȭ �� bfs�Լ� ����
visited = [False] * (n + 1)
bfs(graph, v, visited)