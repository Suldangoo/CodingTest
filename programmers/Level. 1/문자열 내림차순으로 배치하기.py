# 프로그래머스 Lv.1 문자열 내림차순으로 배치하기

def solution(s):
    # 문자열을 리스트로 변환 후 내림차순으로 정렬
    string = sorted(list(s), reverse = True)
    answer = ''.join(string) # 리스트 조인
    
    return answer