# 프로그래머스 Lv.1 문자열 내 p와 y의 개수

def solution(s):
    p = 0 # p의 개수
    y = 0 # y의 개수
    
    for i in s :
        if i in ['p', 'P'] :
            p += 1
        elif i in ['y', 'Y'] :
            y += 1
    
    if p == y :
        return True
    else :
        return False