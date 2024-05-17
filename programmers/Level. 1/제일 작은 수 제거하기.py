# 프로그래머스 Lv.1 제일 작은 수 제거하기

def solution(arr):
    if len(arr) == 1 :
        return [-1]
    else :
        arr.remove(min(arr)) # 가장 작은 값을 제거
        return arr