# 1002. 터렛 (실버 3)
# 알고리즘 분류 : 수학, 기하학, 많은 조건 분기

import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) # 원의 방정식으로 두 원의 거리를 구함

    if distance == 0 and r1 == r2 : # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance: # 두 원이 내접하거나 외접할 때
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2) : # 두 원이 서로 다른 두 점에서 만날 때
        print(2)
    else:
        print(0) # 그 외에