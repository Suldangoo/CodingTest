# 프로그래머스 Lv.1 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    
    for i in str(n) : # 문자열로 변환하여 첫번째부터 삽입
        answer.insert(0, int(i)) # 0번지 배열에 숫자로 변환한 값 삽입
    
    return answer