# 프로그래머스 Lv.1 월간 코드 챌린지 시즌1 : 내적

def solution(a, b):
    answer = 0 # 내적
    
    # 반복문으로 타고들어가 내적을 구함
    for i in range(len(a)) :
        answer += a[i] * b[i]
    
    return answer