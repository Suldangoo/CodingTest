# 프로그래머스 Lv.1 콜라츠 추측

def solution(num):
    epoch = 0 # 연산 시도 횟수
    
    # 500번의 시도
    while epoch < 500 :
        if num == 1 : # 1이라면 연산 횟수 출력
            return epoch
        elif num % 2 == 0 :
            num //= 2
        else :
            num = num * 3 + 1
        epoch += 1
        
    return -1 # 500번동안 결론이 나지 않았다면 -1 출력