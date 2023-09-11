# 프로그래머스 Lv.2 올바른 괄호

def solution(s):
    check = 0
    
    # 스택을 활용
    for i in s :
        if i == '(' :
            check += 1
        elif i == ')' :
            check -= 1
        
        if check < 0 :
            return False
    
    # 0일시 True, 아닐시 False 리턴
    return check == 0