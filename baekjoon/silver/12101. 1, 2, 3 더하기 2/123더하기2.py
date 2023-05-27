# 12101. 1, 2, 3 더하기 2 (실버 1)
# 알고리즘 분류 : 브루트포스 알고리즘, 백트래킹

n, k = map(int, input().split())

max_three = n // 3

for i in range(max_three + 1) :
    num = n - i * 3
    