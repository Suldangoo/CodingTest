# 프로그래머스 Lv.2 124 나라의 숫자

def solution(n):
    digit = [1, 2, 4]
    answer = []
    
    # 1부터 시작하는 3진법이므로, 0 없애고 시작
    n -= 1
    
    # n이 0이 될 때까지 나누어가며 3진수 계산 및 숫자 매핑
    while n >= 0 :
        answer.append(str(digit[n % 3]))
        n = n // 3 - 1 # 값을 하나 감소하여 1부터 시작하는걸 유지
        
    return ''.join(answer[::-1])