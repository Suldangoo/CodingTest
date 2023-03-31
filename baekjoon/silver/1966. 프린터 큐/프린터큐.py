# 1966. �Ѽ� (�ǹ� 3)
# �˰��� �з� : �ڷᱸ��, ť, ����, �ùķ��̼�

import sys
from collections import deque

test = int(sys.stdin.readline())

for _ in range(test) :
    n, m = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))

    queue = deque(importance) # �߿䵵�� �״�� ��� ť ����
    importance.sort() # �߿䵵�� ������������ ����

    i = 1 # ���� ����� ���̰� �� ��°�� ����� �������� üũ�� ����
    # ����Ʈ�� ���̰� 0�� �� ������ �ݺ�
    while(len(importance) > 0) :
        if queue[0] == importance[-1] : # ���� ���� ���� �տ� �ִ� ���̰� ���� �߿䵵�� ���� ���
            del importance[-1] # ���� ���� �߿䵵 ����Ʈ �ϳ� ����
            queue.popleft() # ���� ���
            if m == 0 : # ���� �̹� ���̰� �������� ���̾��ٸ�
                print(i) # i ��� �� break
                break
            else : # �������� ���̰� �ƴ϶��
                i += 1 # ����� ���� ���� ����
                m -= 1 # ���� �������� ���� ���� ����
        else :
            queue.append(queue.popleft()) # �߿䵵�� �� ������ �ִٸ� ���� �ڷ� ��������
            if (m == 0) : # �� ���̰� �������� ���̾��ٸ�
                m = len(importance) - 1 # ���� �ڷ� ����������
            else :
                m -= 1 # �ƴ϶�� �������� ���� ���� ����