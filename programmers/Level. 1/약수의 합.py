# 프로그래머스 Lv.1 약수의 합

def solution(n):
    answer = 0
    
    for i in range(1, n + 1) : # 1부터 n까지의 수 반복
        if n % i == 0 : # 나누어 떨어진다면
            answer += i # 합에 더하기
    
    return answer