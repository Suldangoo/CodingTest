# 1049. 기타줄 (실버 4)
# 알고리즘 분류 : 그리디 알고리즘, 수학

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
six = 1000 # 6줄 패키지 가격중 최솟값
one = 1000 # 1줄 낱개 가격중 최솟값

for _ in range(m) :
    a, b = map(int, input().split())
    # 입력받은 후 최솟값 갱신
    six = min(six, a)
    one = min(one, b)

# 6개 묶음이 낱개를 6개 사는 것보다 쌀 경우
if six < one * 6 :
    # 6개 묶음을 최대한 사고 남은 줄을 낱개로 사는 것 보다 6개 묶음을 하나 더 사는게 더 쌀 경우
    if six < one * (n % 6) :
        print((n // 6 + 1) * six)
    else :
        print((n // 6) * six + (n % 6) * one)
# 6개 묶음보다 낱개로 6개를 사는 것이 더 쌀 경우
else :
    print(n * one)