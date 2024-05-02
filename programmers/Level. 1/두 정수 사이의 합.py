# 프로그래머스 Lv.1 두 정수 사이의 합

def solution(a, b):
    if a <= b :
        nums = list(range(a, b + 1))
    else :
        nums = list(range(b, a + 1))

    return sum(nums)