# 프로그래머스 Lv.1 예산

def solution(d, budget):
    answer = 0
    d.sort() # 필요한 지원이 적은 부서부터 나열
    
    for i in d :
        budget -= i # 예산에서 지원 차감
        if budget >= 0 :
            answer += 1
        else :
            break
    
    return answer