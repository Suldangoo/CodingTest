# 프로그래머스 Lv.2 연속 부분 수열 합의 개수

def solution(elements):
    l = len(elements) # 수열의 길이
    elements *= 2 # 수열 두 개를 하나로 잇기
    sums = set() # 합을 저장할 빈 집합, 중복 불가능
    
    # 1부터 수열의 길이까지 i를 반복, 부분 수열의 사이즈를 결정
    for i in range(1, l + 1) :
        # 0부터 수열의 길이 - 1까지 j를 반복, 부분 수열 시작 번지를 결정
        for j in range(l) :
            sums.add(sum(elements[j:j + i])) # 부분 수열들의 합을 집합에 추가
    
    return len(sums) # 집합의 길이 리턴