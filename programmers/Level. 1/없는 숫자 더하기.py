# 프로그래머스 Lv.1 없는 숫자 더하기

def solution(numbers):
    answer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in numbers :
        answer.remove(i)
    
    return sum(answer)