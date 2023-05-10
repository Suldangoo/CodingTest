# 4949. 균형잡힌 세상 (실버 4)
# 알고리즘 분류 : 자료 구조, 문자열, 스택

while(True) :
    s = input()

    if s == "." : # 온점이라면 프로그램 종료
        break

    stack = [] # 스택 리스트
    result = 'no' # 기본값은 no

    for i in s : # 문자열을 하나씩 살핌
        if i in ['(', '['] : # 여는 괄호라면 그 문자를 스택에 push
            stack.append(i)
        elif i in [')', ']'] :
            # 닫는 괄호일때, 스택이 비어있지 않으며 쌍이 맞을 경우
            if stack and (ord(i) // 10) == (ord(stack[-1]) // 10) :
                # 정상이므로 pop
                stack.pop()
            else :
                # 아닐 경우 반복문 중단
                stack = 1
                break

    # 스택이 empty라면 yes 출력
    if not stack :
        result = 'yes'

    print(result)