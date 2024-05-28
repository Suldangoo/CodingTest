# 프로그래머스 Lv.1 삼총사

def solution(number):
    answer = 0
    
    # 삼총사를 뽑기 위해 세 번의 중첩 반복문 생성
    for i in range(len(number) - 2) :
        for j in range(i + 1, len(number) - 1) :
            for k in range (j + 1, len(number)) :
                if number[i] + number[j] + number[k] == 0 :
                    answer += 1
    
    return answer