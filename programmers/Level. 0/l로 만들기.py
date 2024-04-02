# 프로그래머스 Lv.0 l로 만들기

def solution(myString):
    answer = ''
    filter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'] # l보다 앞선 알파벳들
    
    for i in myString :
        if i in filter : # 필터에 해당되는 알파벳이면 l로 변경
            answer += 'l'
        else : # 아니라면 그대로 더하기
            answer += i
            
    return answer