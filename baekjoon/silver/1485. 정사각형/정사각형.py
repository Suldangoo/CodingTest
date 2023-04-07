# 1485. ���簢�� (�ǹ� 3)
# �˰��� �з� : ������, ����

import math

T = int(input())

for _ in range(T):
    points = []
    for _ in range(4):
        x, y = map(int, input().split())
        points.append((x, y))
    
    # �� �� ������ �Ÿ��� ����Ͽ� ����
    distances = []
    for i in range(3):
        for j in range(i+1, 4):
            d = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
            distances.append(d)
    distances.sort()
    
    # �Ÿ��� ��� ������ ���簢��
    if distances[0] == distances[1] == distances[2] == distances[3]:
        print("1")
    else:
        print("0")