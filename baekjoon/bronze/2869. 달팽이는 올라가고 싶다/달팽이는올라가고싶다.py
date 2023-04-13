# 2869. 달팽이는 올라가고 싶다 (브론즈 1)
# 알고리즘 분류 : 수학

import math

a, b, v = map(int, input().split())

days = math.ceil((v - b) / (a - b))

print(days)