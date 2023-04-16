# 10773. 제로 (실버 4)
# 알고리즘 분류 : 구현, 자료 구조, 스택

import sys

k = int(sys.stdin.readline())
stack = [] # 스택의 역할을 할 빈 리스트 생성

for _ in range(k) :
    n = int(sys.stdin.readline())

    if n == 0 : # 0을 입력받았다면 스택에서 pop
        stack.pop(-1)
    else : # 그 외의 숫자라면 스택에 push
        stack.append(n)

print(sum(stack)) # 스택의 총 합 출력