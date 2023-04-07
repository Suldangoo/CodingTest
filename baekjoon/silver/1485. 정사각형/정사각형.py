# 1485. 정사각형 (실버 3)
# 알고리즘 분류 : 기하학, 정렬

import math

T = int(input())

for _ in range(T):
    points = []
    for _ in range(4):
        x, y = map(int, input().split())
        points.append((x, y))
    
    # 각 점 사이의 거리를 계산하여 정렬
    distances = []
    for i in range(3):
        for j in range(i+1, 4):
            d = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
            distances.append(d)
    distances.sort()
    
    # 거리가 모두 같으면 정사각형
    if distances[0] == distances[1] == distances[2] == distances[3]:
        print("1")
    else:
        print("0")