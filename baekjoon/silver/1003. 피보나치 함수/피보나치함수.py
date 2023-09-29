# 1003. 피보나치 함수 (실버 3)
# 알고리즘 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

# 0과 1의 입력 결과는 이미 정해져있으므로 작성
fibonacci = [[1, 0], [0, 1]]

# 점화식 f(n) = (n - 1) + (n - 2)
for _ in range(39) :
    a = fibonacci[-1][0] + fibonacci[-2][0]
    b = fibonacci[-1][1] + fibonacci[-2][1]
    fibonacci.append([a, b])

for _ in range(int(input())) :
    # 입력받는 숫자 번지의 0 출력 갯수와 1 출력 갯수를 출력
    result = fibonacci[int(input())]
    print(result[0], result[1])