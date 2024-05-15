# 프로그래머스 Lv.2 의상

def solution(clothes):
    wears = dict() # 의상 종류 : 의상 이름의 딕셔너리
    
    # 의상 개수만큼 반복
    for wear in clothes :
        if wear[1] in wears : # 의상 종류가 이미 있다면 해당 의상 추가
            wears[wear[1]].append(wear[0])
        else : # 없다면 해당 의상 종류를 새로 등록
            wears[wear[1]] = [wear[0]]
    
    answer = 1 # 곱해야 하기 때문에 1로 초기화
    
    # 조합식
    for i in wears :
        answer *= len(wears[i]) + 1 # 해당 의상 종류를 안 입은 것도 경우의 수이므로 +1
    
    return answer - 1 # 아무런 의상도 입지 않은 경우의 수 제외