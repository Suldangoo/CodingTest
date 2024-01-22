# 프로그래머스 Lv.0 옹알이 (1)

def solution(babbling):
    cant = 0 # 발음 불가능한 단어의 개수
    two = ["ye", "ma"] # 두 글자의 옹알이
    three = ["aya", "woo"] # 세 글자의 옹알이
    
    # 한 단어씩 살펴보기
    for ward in babbling :
        while len(ward) : # ward 단어가 남아있다면 실행
            # 1번 조건 : ward가 두 글자 이상이며, 두 글자의 옹알이를 포함할 경우 성공
            if len(ward) >= 2 and ward[:2] in two :
                ward = ward[2:]
            # 2번 조건 : ward가 세 글자 이상이며, 세 글자의 옹알이를 포함할 경우
            elif len(ward) >= 3 and ward[:3] in three :
                ward = ward[3:]
            else :
                cant += 1
                break
    
    return len(babbling) - cant # 총 단어의 개수에서 발음 실패한 단어를 빼기