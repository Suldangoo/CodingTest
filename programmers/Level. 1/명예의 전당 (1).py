# 프로그래머스 Lv.1 명예의 전당 (1)

def solution(k, score):
    answer = []
    memory = []
    
    for i in score :
        memory.append(i) # 메모리에 점수를 추가
        
        if len(memory) <= k : # 아직 메모리가 덜 찼다면 최하위 점수를 삽입
            answer.append(min(memory))
        else :
            memory.sort(reverse = True)
            answer.append(min(memory[:k])) # 상위 k까지의 점수에서 가장 낮은 점수를 출력
    
    return answer