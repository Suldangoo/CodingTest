# 2178. �̷� Ž�� (�ǹ� 1)
# �˰��� �з� : �׷��� �̷�, �׷��� Ž��, �ʺ� �켱 Ž��

import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n * m + 1)]
numList = []

for _ in range(n) :
    numList.append(sys.stdin.readline())

for i in range(n) :
    for j in range(m - 1) :
        if numList[i][j] + numList[i][j] == 2 :
            graph[i * m + j + 1].append(i * m + j + 2)
            graph[i * m + j + 2].append(i * m + j + 1)

