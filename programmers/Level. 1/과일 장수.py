# 프로그래머스 Lv.1 과일 장수

def solution(k, m, score):
    answer = 0 # 누적 이익값
    score.sort(reverse = True) # 사과를 내림차순으로 정렬
    
    n = m - 1 # 포인터
    while n < len(score) :
        answer += score[n] * m # 최저사과 점수 * 사과 개수 값을 이익에 누적
        n += m # 포인터 증감
          
    return answer