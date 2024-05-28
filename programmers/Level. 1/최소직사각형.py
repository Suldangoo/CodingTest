# 프로그래머스 Lv.1 최소직사각형

def solution(sizes):
    w = [] # 모든 명함의 가로 길이
    h = [] # 모든 명함의 세로 길이
    
    for i in sizes :
        i.sort() # 내림차순으로 정렬
        w.append(i[0]) # 가로 길이에 짧은 길이를 삽입
        h.append(i[1]) # 세로 길이에 긴 길이를 삽입
        
    return max(w) * max(h)