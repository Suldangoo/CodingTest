# 프로그래머스 Lv.1 두 개 뽑아서 더하기

def solution(numbers):
    answer = set() # 중복이 없게끔 set으로 설정
    
    # 완전탐색
    for i in range(len(numbers) - 1) :
        for j in range(i + 1, len(numbers)) :
            answer.add(numbers[i] + numbers[j])
    
    return sorted(list(answer)) # 리스트로 전환