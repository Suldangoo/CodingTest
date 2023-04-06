# 1764. �躸�� (�ǹ� 4)
# �˰��� �з� : �ڷ� ����, ���ڿ�, ����

import sys

n, m = map(int, sys.stdin.readline().split())

nameDict = {} # �赵 ���� ����� �̸��� ���� �ؽ� (��ųʸ�)
nameList = [] # �赵 ���� ���� ������� �̸��� ���� ����Ʈ

for i in range(n):
    name = sys.stdin.readline().strip()
    nameDict[name] = 1 # �ؽÿ� �赵 ���� ����� �̸��� �Ҵ�

for i in range(m):
    name = sys.stdin.readline().strip()

    # �ؽ�(��ųʸ�) �ȿ��� in���� ���ϴ� key�� ã�� ���� �ɸ��� �ð� ���⵵�� O(1)
    if name in nameDict:
        nameList.append(name)

# ������ ����
nameList.sort()

print(len(nameList))
for name in nameList:
    print(name)