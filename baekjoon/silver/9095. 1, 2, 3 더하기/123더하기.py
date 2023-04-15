# 9095. 1, 2, 3 더하기 (실버 3)
# 알고리즘 분류 : 다이나믹 프로그래밍

import sys

# 정답 리스트에 정수 1, 2, 3을 만드는 방법의 개수를 미리 삽입
ansList = [1, 2, 4]

# 정수 4 ~ 10까지의 방법의 개수를 DP로 구현
for i in range(3, 10) :
    # 점화식 A(n) = A(n - 1) + A(n - 2) + A(n - 3)
    num = ansList[i - 1] + ansList[i - 2] + ansList[i - 3]
    ansList.append(num)

t = int(sys.stdin.readline())

for _ in range(t) :
    n = int(sys.stdin.readline())
    print(ansList[n - 1])