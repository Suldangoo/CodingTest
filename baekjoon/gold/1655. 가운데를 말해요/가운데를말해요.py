# 1655. ����� ���ؿ� (���2)
# �˰��� �з� : �켱���� ť, ��, �ڷᱸ��

import heapq # ��ť ��� ���
import sys

# �Է¹ޱ�
n = int(sys.stdin.readline().strip())
nums = []

# �߾Ӱ� �������� ���� ������ max_heap��, ū ������ min_heap�� ����
max_heap = [] # �ִ� ��
min_heap = [] # �ּ� ��

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    # ¦�� ��° ���� ���
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num)) # �ִ� ���� ����
    # Ȧ�� ��° ���� ���
    else:
        heapq.heappush(min_heap, (num, num)) # �ּ� ���� ����

    # �ִ� ���� �ִ��� �ּ� ���� �ּڰ����� Ŭ ��� �� ���� ��ȯ
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-min_value, min_value))
        heapq.heappush(min_heap, (max_value, max_value))
    
    # �߾Ӱ� ���
    print(max_heap[0][1])