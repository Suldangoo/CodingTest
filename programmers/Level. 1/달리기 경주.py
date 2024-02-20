# 프로그래머스 Lv.1 달리기 경주

def solution(players, callings):
    rank = {string : i for i, string in enumerate(players)}
    
    for i in callings : # 부른 이름을 하나씩 가져오기
        n = rank[i] # 호명된 선수의 기존 등수
        rank[i] -= 1 # 추월한 선수의 등수를 1 감소
        rank[players[n - 1]] += 1 # 추월당한 선수의 등수를 1 증가
        
        players[n - 1], players[n] = players[n], players[n - 1] # 두 선수의 위치 변경
                
    return players