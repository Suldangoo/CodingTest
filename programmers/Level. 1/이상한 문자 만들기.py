# 프로그래머스 Lv.1 이상한 문자 만들기

def solution(s):
    sList = list(s)
    F = False # Flip Flop
    
    for i in range(len(sList)) :
        F = not F # Flip Flop 뒤집기
        
        if sList[i] == ' ' : # 공백이라면 Flip Flop 초기화
            F = False
        elif F :
            sList[i] = sList[i].upper()
        else :
            sList[i] = sList[i].lower()
    
    s = ''.join(sList) # 리스트 다시 문자열로 합치기
    
    return s