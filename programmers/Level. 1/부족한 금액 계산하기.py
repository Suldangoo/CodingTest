# 프로그래머스 Lv.1 부족한 금액 계산하기

def solution(price, money, count):
    # 1부터 count까지의 합 구하기
    total_count = count * (count + 1) / 2
    
    # 현재 돈에서 놀이기구 총 이용료를 빼고 음양수를 뒤집기, 0보다 작다면 0을 출력
    return max(-(money - price * total_count), 0)