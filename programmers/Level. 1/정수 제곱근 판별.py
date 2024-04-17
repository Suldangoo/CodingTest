# 프로그래머스 Lv.1 정수 제곱근 판별

import math

def solution(n):
    x = math.sqrt(n) # 제곱근을 계산
    
    # int로 변환했을 때 원본과 값이 같다면 나누어 떨어진 것으로 판단
    if x == int(x) :
        return math.pow(x + 1, 2) # 제곱 값 리턴
    else :
        return -1 # -1 리턴