# 프로그래머스 Lv.1 x만큼 간격이 있는 n개의 숫자

def multiply(x, n):
    # 두 리스트를 곱한 컴프리헨션을 만드는 함수
    return [x * (i+1) for i in range(n)]

def solution(x, n):
    return multiply(x, n)