# 10845. 큐 (실버 4)
# 알고리즘 분류 : 자료구조, 큐

from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque()

for _ in range(n) :
    # 반복문 안에서 입력문을 작성할 땐 반드시 sys를 사용할 것
    command = list(sys.stdin.readline().split())

    if command[0] == "push" :
        queue.append(command[1])
    elif command[0] == "pop" :
        print(queue.popleft()) if len(queue) != 0 else print(-1)
    elif command[0] == "size" :
        print(len(queue))
    elif command[0] == "empty" :
        print(0 if len(queue) >= 1 else 1)
    elif command[0] == "front" :
        print(queue[0]) if len(queue) != 0 else print(-1)
    elif command[0] == "back" :
        print(queue[-1]) if len(queue) != 0 else print(-1)