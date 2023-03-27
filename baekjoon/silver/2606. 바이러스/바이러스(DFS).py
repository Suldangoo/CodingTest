# 2606. ���̷��� (�ǹ� 3)
# �˰��� �з� : DFS, BFS, �׷��� �̷�

# ����Լ��� �̿��� DFS�� Ǯ��
def dfs(graph, v, visited) :
    visited[v] = True

    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

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
dfs(graph, 1, visited)
print(visited.count(True) - 1) # 1�� ��ǻ�͸� ������ ���̷����� �ɸ� ��ǻ���� ���� ���