# 1107. 리모컨 (골드 5)
# 알고리즘 분류 : 브루트포스

import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
broken = []
if m > 0 :
    broken = list(map(int, sys.stdin.readline().rstrip().split()))

ans = abs(n - 100)

for i in range(n, 500001) :
    for j in str(i) :
        if not j in broken :
            ans = ans if ans < len(i) else len(i)
        ans = ans if ans < n - 100 else n - 100

for i in range(0, n) :
    for j in str(i) :
        if not j in broken :
            ans = ans if ans < len(i) else len(i)
        ans = ans if ans < n - 100 else n - 100

print(ans)