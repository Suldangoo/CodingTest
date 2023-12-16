# 프로그래머스 Lv.1 문자열 내 마음대로 정렬하기

def solution(strings, n):
    sortString = sorted(strings) # 사전순으로 정렬된 문자열 리스트
    charlist = [] # 원하는 글자와 해당 데이터의 인덱스가 들어가는 리스트
    answer = [] # 정답 리스트
    
    num = 0
    
    for i in sortString :
        charlist.append([i[n], num])
        num += 1
    
    charlist = sorted(charlist)
    
    for i in charlist :
        answer.append(sortString[i[-1]])
        
    return answer