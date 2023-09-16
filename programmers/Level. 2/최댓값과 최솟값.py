# 프로그래머스 Lv.2 최댓값과 최솟값

def solution(s):
    answer = ''
    # 입력된 숫자들을 분할하고 int로 변환
    nums = list(map(int, s.split()))
    
    # 최솟값과 최댓값을 구한 후 문자열에 합병
    answer = str(min(nums)) + ' ' + str(max(nums))
    return answer