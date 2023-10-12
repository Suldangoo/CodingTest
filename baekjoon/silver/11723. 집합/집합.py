# 11723. 집합 (실버 5)
# 알고리즘 분류 : 구현, 비트마스킹

import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M) :
    command = list(input().split())

    if command[0] == "add" :
        S.add(int(command[1]))
    elif command[0] == "remove" :
        if int(command[1]) in S :
            S.remove(int(command[1]))
    elif command[0] == "check" :
        print(1 if (int(command[1]) in S) else 0)
    elif command[0] == "toggle" :
        if int(command[1]) in S :
            S.remove(int(command[1]))
        else :
            S.add(int(command[1]))
    elif command[0] == "all" :
        S = set(list(range(1, 21)))
    elif command[0] == "empty" :
        S = set()
    elif command[0] == "print" :
        print(S)