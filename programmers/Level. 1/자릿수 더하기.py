# 프로그래머스 Lv.1 자릿수 더하기

def solution(n):
    answer = 0

    while n > 0 :
        answer += n % 10 # 10의 나머지를 더하기
        n //= 10 # 10으로 몫나눗셈
    
    return answer