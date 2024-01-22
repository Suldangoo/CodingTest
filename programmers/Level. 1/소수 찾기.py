# 프로그래머스 Lv.1 소수 찾기

def solution(n):
    # 번지값이 소수인지 판별하는 is_prime 리스트 생성
    is_prime = [True] * (n + 1)
    
    # 0과 1은 소수가 아니므로 False로 지정
    is_prime[0] = is_prime[1] = False
    
    # 에라토스테네스의 체를 사용하여 소수 탐색
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    
    return sum(is_prime) # 소수의 개수 리턴