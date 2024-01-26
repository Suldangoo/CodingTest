# 프로그래머스 Lv.1 체육복

def solution(n, lost, reserve):
    
    team = {}
    count = 0
    
    for i in range(n) :
        team[i] = 1
        if i + 1 in lost :
            team[i] -= 1
        if i + 1 in reserve :
            team[i] += 1
            
    if team[0] == 2 and team[1] == 0 :
        team[0] -= 1
        team[1] += 1

    if team[n-1] == 2 and team[n-2] == 0 :
        team[n-1] -= 1
        team[n-2] += 1

    for i in range(1, n-1) :
        if team[i] == 2 and team[i - 1] == 0 :
            team[i] -= 1
            team[i - 1] += 1
        elif team[i] == 2 and team[i + 1] == 0 :
            team[i] -= 1
            team[i + 1] += 1
            
    for k, v in team.items() :
        if v >= 1 :
            count += 1
            
    return count