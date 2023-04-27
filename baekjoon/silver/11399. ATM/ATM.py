# 11399. ATM (실버 4)
# 알고리즘 분류 : 그리디 알고리즘

import sys

n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().rstrip().split()))

# 시간이 적게 드는 사람부터 인출하면 되므로 우선 정렬
time = sorted(time)
total = 0 # 누적 시간 값을 더할 변수

for i in range(n + 1) : # n + 1까지 반복
    total += sum(time[:i]) # 처음부터 n까지 슬라이싱 후 누적

print(total)