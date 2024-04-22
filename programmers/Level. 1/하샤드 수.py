# 프로그래머스 Lv.1 하샤드 수

def solution(x):
    num = x
    sums = 0
    
    # 모든 자릿수의 합 구하기
    while num > 0 :
        sums += num % 10
        num //= 10
        
    # 나누어 떨어지면 True 출력
    if x % sums == 0 :
        return True
    else :
        return False