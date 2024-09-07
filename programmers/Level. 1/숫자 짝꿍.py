# 프로그래머스 Lv.1 숫자 짝꿍

from collections import Counter

def solution(X, Y):
    # X와 Y의 각 숫자의 빈도를 계산
    X_count = Counter(X)
    Y_count = Counter(Y)
    
    # X와 Y에서 공통으로 등장하는 숫자들 중 최소 빈도만큼 추출하여 내림차순 정렬
    common_nums = sorted((min(X_count[num], Y_count[num]) * num for num in X_count if num in Y_count), reverse=True)
    
    # 공통 숫자가 없으면 "-1" 반환
    if not common_nums:
        return "-1"
    
    answer = ''.join(common_nums)
    
    # "0"으로만 이루어진 경우 "0" 반환
    return "0" if answer[0] == "0" else answer