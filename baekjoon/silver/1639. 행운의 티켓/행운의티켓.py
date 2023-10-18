# 1639. 행운의 티켓 (실버 4)
# 알고리즘 분류 : 구현, 브루트포스 알고리즘

import sys
input = sys.stdin.readline

def isEqual(num) : # 왼쪽 N자리와 오른쪽 N자리의 합을 비교
    asum = sum(num[:len(num) // 2])
    bsum = sum(num[len(num) // 2:])

    if asum == bsum :
        return True
    else :
        return False

S = list(map(int, list(input().strip())))
best = 0 # 최대 길이

for i in range(len(S) - 1) : # 0번지부터 최대길이 - 1번지까지를 시작지점으로
    for j in range(i + 1, len(S)) : # 시작지점부터 최대길이 번지까지를 끝지점으로
        if (j - i) % 2 == 1 : # 측정할 전체 길이가 짝수라면
            if isEqual(S[i : j]) :
                best = max(best, (j - i) + 1)

print(best)