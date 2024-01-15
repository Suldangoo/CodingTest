# 프로그래머스 Lv.1 소수 만들기

def solution(nums):
    answer = 0 # 소수의 개수
    
    # 3개의 연속된 좌표값 완전탐색
    for i in range(len(nums) - 2) :
        for j in range(i + 1, len(nums) - 1) :
            for k in range(j + 1, len(nums)) :
                num = nums[i] + nums[j] + nums[k] # 합 구하기
                
                # 2부터 num까지 반복 (1 이상의 자연수를 3번 더하기 때문에, 합값의 최솟값이 3)
                for n in range(2, num) :
                    if num % n == 0 : # 한 번이라도 나누어떨어진다면 즉시 반복문 종료
                        break
                    elif n == num - 1 : # 마지막까지 도달했다면 소수 판정, answer값 증가
                        answer += 1
    
    return answer