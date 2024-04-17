# 프로그래머스 Lv.1 정수 내림차순으로 배치하기

def solution(n):
    nums = []
    
    while n > 0 :
        nums.append(n % 10) # 각 자릿수별로 분해하여 배열에 삽입
        n //= 10
        
    nums = sorted(nums, reverse = True) # 내림차순 정렬
    
    return int(''.join(map(str, nums))) # 문자형으로 변환하여 합친 후 숫자형으로 변환