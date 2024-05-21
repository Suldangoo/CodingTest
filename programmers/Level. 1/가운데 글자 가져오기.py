# 프로그래머스 Lv.1 가운데 글자 가져오기

def solution(s):
    slen = len(s) # 문자열의 길이
    
    if slen % 2 == 0 : # 짝수라면
        return s[slen//2 - 1:slen//2 + 1]
    else : # 홀수라면
        return s[slen//2]