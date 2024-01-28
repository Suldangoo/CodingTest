# 프로그래머스 Lv.1 체육복

def solution(n, lost, reserve):
    
    team = {} # 팀 딕셔너리
    count = 0 # 최종 진출 가능 팀
    
    # 팀에 체육복 배분
    for i in range(n) :
        team[i] = 1
        if i + 1 in lost :
            team[i] -= 1
        if i + 1 in reserve :
            team[i] += 1
            
    # 배열 바깥 처리를 위한 예외 처리
    if team[0] == 2 and team[1] == 0 :
        team[0] -= 1
        team[1] += 1

    if team[n-1] == 2 and team[n-2] == 0 :
        team[n-1] -= 1
        team[n-2] += 1

    # 좌우에 비어있는 사람이 있다면, 체육복 대여
    for i in range(1, n-1) :
        if team[i] == 2 and team[i - 1] == 0 :
            team[i] -= 1
            team[i - 1] += 1
        elif team[i] == 2 and team[i + 1] == 0 :
            team[i] -= 1
            team[i + 1] += 1
            
    # 최종적으로 체육복이 1개 이상 있는 사람의 수를 카운트
    for k, v in team.items() :
        if v >= 1 :
            count += 1
            
    return count