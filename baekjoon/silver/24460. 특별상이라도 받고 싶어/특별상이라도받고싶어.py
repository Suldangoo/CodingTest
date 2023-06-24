# 24460. 특별상이라도 받고 싶어 (실버 3)
# 알고리즘 분류 : 분할 정복, 재귀

import sys

# def Award(chairs, n) :
#     if n == 2 :


N = int(sys.stdin.readline())
chairs = []

for i in range(N) :
    chairs.append(list(map(int, sys.stdin.readline().split())))

for i in chairs :
    for j in i :
        print(j, end = ' ')
    print()