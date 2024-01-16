# 프로그래머스 Lv.1 모의고사

def solution(answers):
    
    one = [1, 2, 3, 4, 5] # 1번 수포자의 최소 반복배열
    two = [2, 1, 2, 3, 2, 4, 2, 5] # 2번 수포자의 최소 반복배열
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번 수포자의 최소 반복배열
    
    score = [0, 0, 0] # 각각 1번, 2번, 3번 수포자의 정답 점수
    
    for i in answers :
        # 각 수포자들의 정답 배열 맨 첫 번째 번지의 수로 채점
        if one[0] == i :
            score[0] += 1
        if two[0] == i :
            score[1] += 1
        if three[0] == i :
            score[2] += 1
    
        # 각자의 정답 배열 앞 정답을 뒤로 넘기기
        one.append(one.pop(0))
        two.append(two.pop(0))
        three.append(three.pop(0))
    
    best = max(score) # 최고 점수 측정
    answer = [] # 최고점수를 받은 사람들을 담을 배열
    
    for i in range(3) :
        if score[i] == best : # 최고점수라면, answer에 해당 수포자의 번호 추가
            answer.append(i + 1)
    
    return answer