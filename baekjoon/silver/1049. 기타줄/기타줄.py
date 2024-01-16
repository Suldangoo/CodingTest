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

answer = n * one # 기본값을 모두 낱개로 샀을 때 값으로 설정

# 6줄 패키지를 최소 1개 샀을 때부터, 사야하는 줄 갯수를 모두 채울 수 있을 때까지 i 증가하며 반복
for i in range(1, (n + 5) // 6 + 1) :
    if n - i * 6 > 0 : # 6줄 패키지만으로 줄 수를 모두 채울 수 있는지 확인
        tmp = n - i * 6
    else :
        tmp = 0

    # 최솟값 책정
    answer = min(answer, six * i + one * tmp)

print(answer)