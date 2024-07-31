# 프로그래머스 Lv.1 K번째수

def solution(array, commands):
    answer = []
    
    for i in commands :
        # 인덱싱이 0부터 시작함을 고려
        tmp = sorted(array[i[0] - 1 : i[1]])
        answer.append(tmp[i[2] - 1])
    
    return answer