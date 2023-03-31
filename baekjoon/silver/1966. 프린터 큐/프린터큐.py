# 1966. �Ѽ� (�ǹ� 3)
# �˰��� �з� : �ڷᱸ��, ť, ����, �ùķ��̼�

import sys
from collections import deque

test = int(sys.stdin.readline())

for _ in range(test) :
    n, m = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))

    queue = deque(importance)
    importance.sort()

    i = 1

    while(len(importance) > 0) :
        if queue[0] == importance[-1] :
            del importance[-1]
            queue.popleft()
            if m == 0 :
                print(i)
                break
            else :
                i += 1
                m -= 1
        else :
            queue.append(queue.popleft())
            if (m == 0) :
                m = len(importance) - 1
            else :
                m -= 1