# 프로그래머스 Lv.1 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    arr = sorted(arr) # 리스트를 정렬
    answer = []
    
    for i in arr :
        if i % divisor == 0 :
            answer.append(i) # 나누어 떨어진다면 추가
    
    if len(answer) > 0 :
        return answer
    else : # 정답 리스트의 길이가 0이라면 [-1] 리턴
        return [-1]