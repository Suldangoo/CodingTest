# 프로그래머스 Lv.1 폰켓몬

def solution(nums):
    nums_set = set(nums) # 중복 제거
    
    # 폰켓몬의 종류와 가져갈 수 있는 폰켓몬의 수 중 낮은 수를 출력
    return min(len(nums_set), len(nums) // 2)