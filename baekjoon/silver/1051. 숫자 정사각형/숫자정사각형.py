# 1051. 숫자 정사각형 (실버 4)
# 알고리즘 분류 : 브루트포스

import sys
n, m = map(int, sys.stdin.readline().split())
small_side = min(n, m)

squar = []
for _ in range(n) :
    nums = []
    num = sys.stdin.readline()
    for i in num :
        nums.append(i)
    squar.append(nums)

for i in reversed(range(1, small_side + 1)) : # 한 변의 길이가 i인 정사각형 체크, i는 n부터 1까지 낮아짐
    for a in range(n - i + 1) : # 열이 몇 번째 칸까지 존재할 수 있는지 체크, a는 0부터 n - i까지 돌게 됨
        for b in range(m - i + 1) : # 행이 몇 번째 칸까지 존재할 수 있는지 체크, b는 0부터 m - i까지 돌게 됨
            if(squar[a][b] == squar[a][b + i - 1] and
               squar[a][b] == squar[a + i - 1][b] and
               squar[a][b] == squar[a + i - 1][b + i - 1]) :
                print(i * i)
                exit(0)