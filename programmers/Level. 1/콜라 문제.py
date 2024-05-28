# 프로그래머스 Lv.1 콜라 문제

def solution(a, b, n):
    answer = 0
    
    # 남은 콜라 병 수가 반환 가능한 수 미만이 될 때까지 반복
    while n > a - 1 :
        answer += (n // a) * b # 우선 받은 콜라를 answer에 누적
        n = (n // a) * b + (n % a) # 남은 콜라 병 수를 갱신
    
    return answer