# 프로그래머스 Lv.1 추억 점수

def solution(name, yearning, photo):
    score = dict()
    
    for i in range(len(name)) :
        score[name[i]] = yearning[i] # 딕셔너리에 값 할당
    
    answer = [] # 사진별 점수를 합할 결과 리스트
    
    for i in photo :
        sumScore = 0
        for j in i :
            # 딕셔너리에 이름이 존재하면 값 할당
            if j in score :
                sumScore += score[j]
        
        answer.append(sumScore) # 점수 추가
    
    return answer