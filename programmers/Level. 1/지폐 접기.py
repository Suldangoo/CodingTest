# PCCP 기출문제 9번
# 프로그래머스 Lv.1 지폐 접기

def solution(wallet, bill):
    answer = 0
    
    while max(bill) > max(wallet) or min(bill) > min(wallet) :
        bill.sort();
        bill[1] //= 2
        answer += 1
    
    return answer