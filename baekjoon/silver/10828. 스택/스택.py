# 10828. 스택 (실버 4)
# 알고리즘 분류 : 자료구조, 스택

import sys
n = int(sys.stdin.readline())
stack = [] # 스택 역할을 하게 될 리스트

for _ in range(n) :
    # 반복문 안에서 입력문을 작성할 땐 반드시 sys를 사용할 것
    command = list(sys.stdin.readline().split())

    if command[0] == "push" :
        stack.append(command[1])
    elif command[0] == "pop" :
        print(stack.pop()) if len(stack) != 0 else print(-1)
    elif command[0] == "size" :
        print(len(stack))
    elif command[0] == "empty" :
        print(0 if len(stack) >= 1 else 1)
    else : # top 명령어인 경우
        print(stack[-1]) if len(stack) != 0 else print(-1)