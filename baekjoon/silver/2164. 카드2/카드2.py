# 2164. ī��2 (�ǹ� 4)
# �˰��� �з� : �ڷᱸ��, ť

# collections.deque ��ũ ���̺귯�� ���
from collections import deque

n = int(input())
card = deque() # ���ο� ť ����

# ����ڰ� �Է��� ���ڸ�ŭ�� ī�� ����
for i in range(n) :
    card.append(i + 1)

# ī�尡 �� �� ���� ������ �ݺ�
while(len(card) > 1) :
    card.popleft() # ���� ������ ī�带 ����
    card.append(card.popleft()) # ���� ������ ī�带 �����ϸ鼭 ������ �߰�

print(card[0]) # ������ ���� ī�� �ϳ��� ���