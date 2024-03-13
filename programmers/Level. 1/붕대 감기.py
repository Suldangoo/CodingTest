# 프로그래머스 Lv.1 붕대 감기
# PCCP 기출문제

def solution(bandage, health, attacks):
    hp = health # health는 최대 체력으로 두고, 현재 hp를 의미하는 변수 생성
    time = 0 # 연속으로 성공하는 시간
    
    # 가장 마지막 공격의 공격 시간 초까지 반복
    for t in range(1, attacks[-1][0] + 1) :
        # 몬스터의 공격 시간인지 체크
        if t == attacks[0][0] :
            hp -= attacks[0][1] # 현재 hp에 데미지
            # 캐릭터가 죽었다면 hp를 -1로 만든 후 반복문 종료
            if hp <= 0 :
                hp = -1
                break
            time = 0 # 연속 성공 초기화
            attacks.pop(0) # 몬스터의 가장 최근 공격이 실행되었으므로 리스트에서 제거
            
        # 몬스터의 공격 시간이 아니라면, 회복
        else :
            hp = min(hp + bandage[1], health) # hp 회복 후 최대 체력을 넘지 않도록 조정
            time += 1 # 연속 성공 시간 증가
            # 연속 성공 시간이 되었다면 hp 회복 후 연속 성공 시간 초기화
            if time >= bandage[0] :
                hp = min(hp + bandage[2], health) # hp 회복 후 최대 체력을 넘지 않도록 조정
                time = 0
            
    return hp # 남은 hp 리턴