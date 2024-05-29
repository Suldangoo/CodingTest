# 프로그래머스 Lv.1 카드 뭉치

def solution(cards1, cards2, goal):
    for i in goal :
        # 카드의 덱에 카드가 남아있고, 제일 앞에 카드와 같은지 비교
        if len(cards1) > 0 and i == cards1[0] :
            cards1.pop(0)
        elif len(cards2) > 0 and i == cards2[0] :
            cards2.pop(0)
        else :
            return "No"
    
    return "Yes"