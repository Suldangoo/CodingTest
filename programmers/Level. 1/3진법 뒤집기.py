# 프로그래머스 Lv.1 3진법 뒤집기

def solution(n):
    answer = 0
    ternary = []
    
    # n이 0이 될 때까지 실행
    while n :
        ternary.append(n % 3) # 뒤에서부터 추가했으므로 앞뒤 반전된 상태로 진행
        n //= 3
    
    num = 1 # 3씩 곱해질 수
    
    # 원래 3진법 형태로 뒤집은 후 연산
    for i in reversed(ternary) :
        answer += i * num
        num *= 3
    
    return answer