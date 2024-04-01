# 프로그래머스 Lv.1 가장 가까운 같은 글자

def solution(s):
    index = {} # 알파벳들의 마지막 위치 저장 딕셔너리
    answer = []
    
    for idx, alp in enumerate(s) :
        if alp not in index :
            answer.append(-1)
        else :
            answer.append(idx - index[alp]) # 현재 위치 - 마지막 위치
            
        index[alp] = idx # 현재 알파벳의 위치 갱신
    
    return answer