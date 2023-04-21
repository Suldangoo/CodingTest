# 9012. 괄호 (실버 4)
# 알고리즘 분류 : 자료 구조, 문자열, 스택

import sys

t = int(sys.stdin.readline())

for _ in range(t) :
    bracket = sys.stdin.readline().rstrip()
    stack = 0 # VPS를 판정할 스택
    vps = "YES" # 기본값은 YES
    for i in bracket :
        if i == '(' : # 여는 괄호일 때 1 증가
            stack += 1
        if i == ')' : # 닫는 괄호일 때 1 감소
            stack -= 1
        if stack < 0 : # 스택이 음수가 되는 순간 NO로 판정 종료
            vps = "NO"
            break
    if stack != 0 : # 스택이 empty가 아니라면 NO
        vps = "NO"
    print(vps)