# 2606. ���̷��� (�ǹ� 3)
# �˰��� �з� : DFS, BFS, �׷��� �̷�

# deque�� �̿��� BFS�� Ǯ��
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

computer = int(input()) # ��ǻ���� ����
link = int(input()) # ����� ��ǻ�� ������� ����

# ��ǻ���� ������ŭ �� ����Ʈ�� �ʱ�ȭ
graph = [[] for _ in range(computer + 1)]

# ����� �Է� �ޱ�
for i in range(link):
    a, b = map(int, input().split())
    # a�� ��ǻ�Ϳ� b�� ����Ǿ��ְ�, b�� ��ǻ�Ϳ� a�� ����Ǿ������� �߰�
    graph[a].append(b)
    graph[b].append(a)

# �湮 üũ ����Ʈ�� ��� False�� ��ǻ�� ������ŭ �ʱ�ȭ
visited = [False] * (computer + 1)

# dfs �Լ� ����
bfs(graph, 1, visited)
print(visited.count(True) - 1) # 1�� ��ǻ�͸� ������ ���̷����� �ɸ� ��ǻ���� ���� ���