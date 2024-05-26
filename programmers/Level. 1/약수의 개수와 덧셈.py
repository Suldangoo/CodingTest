# 프로그래머스 Lv.1 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    
    # left부터 right까지 모든 수에 대해 반복
    for i in range(left, right + 1) :
        divisor = 1 # 약수의 개수 변수 초기화, 자기 자신은 미리 포함
        for j in range(1, i) :
            if i % j == 0 :
                divisor += 1
        
        # 약수의 개수가 짝수라면 더하고, 홀수라면 빼기
        if divisor % 2 == 0 :
            answer += i
        else :
            answer -= i
    
    return answer