# 프로그래머스 Lv.1 시저 암호

def solution(s, n):
    # 아스키코드 변환 메서드인 ord()와 chr() 응용
    sList = list(s)
    
    for i in range(len(sList)) :
        if sList[i] == ' ' : # 공백인 경우 패스
            continue
            
        if ord(sList[i]) in range(65, 91) : # 대문자인 경우
            tmp = (ord(sList[i]) - 65 + n) % 26
            sList[i] = chr(tmp + 65)
        elif ord(sList[i]) in range(97, 123) : # 소문자인 경우
            tmp = (ord(sList[i]) - 97 + n) % 26
            sList[i] = chr(tmp + 97)
    
    return ''.join(sList)