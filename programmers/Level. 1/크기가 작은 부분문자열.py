# 프로그래머스 Lv.1 3진법 뒤집기

def solution(t, p):
    answer = 0
    length = len(p)
    
    # t의 길이 - p의 길이까지 좌표를 순환
    for i in range(len(t) - length + 1) :
        # 부분 문자열을 구한 후 int 변환하여 대소비교
        if int(t[i:i + length]) <= int(p) :
            answer += 1
    
    return answer