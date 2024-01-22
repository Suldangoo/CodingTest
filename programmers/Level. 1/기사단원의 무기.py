# 프로그래머스 Lv.1 기사단원의 무기

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1) :
        n = 0 # 약수의 개수 초기화
        
        # i의 제곱근까지의 약수를 구해 빠르게 약수의 개수 정리
        for j in range(1, int(i ** 0.5) + 1) :
            if j ** 2 == i :
                n += 1
            elif i % j == 0 :
                n += 2
                
        # 제한수치를 초과할 경우, 그 약수의 개수를 power로 교체
        if n > limit :
            answer += power
        else :
            answer += n
    
    return answer