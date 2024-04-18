# 프로그래머스 Lv.1 문자열 다루기 기본

def solution(s):
    # s가 숫자의 형태인가? AND (길이가 4인가? OR 길이가 6인가?)
    return s.isdecimal() and (len(s) == 4 or len(s) == 6)