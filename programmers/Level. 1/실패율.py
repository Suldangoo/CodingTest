# 프로그래머스 Lv.1 실패율
# 2019 KAKAO BLIND RECRUITMENT

def solution(N, stages):
    
    users = len(stages) # 총 게임 이용자
    fail = [] # 각 스테이지별 실패율
    
    for i in range(1, N + 1) : # 1부터 N까지의 스테이지 탐색
        if users > 0 : # 남은 유저수가 있을 때
            user = stages.count(i) # 해당 스테이지를 도전하려는 유저수 측정
            fail.append(user / users) # 실패율 계산 및 추가
            users -= user # 총 유저수에서 다음 스테이지로 간 유저를 추리기
        else : # 남은 유저수가 없다면
            fail.append(0) # 도달한 유저수가 없다면 해당 스테이지 실패율은 0으로 정의
    
    answer = sorted(range(len(fail)), key=lambda i: (fail[i], -i), reverse=True) # 값을 내림차순으로 하여금 번지수를 구함
    answer = [index + 1 for index in answer] # 모든 요소에 1을 더하기

    return answer