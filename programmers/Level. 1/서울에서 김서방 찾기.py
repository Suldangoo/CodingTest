# 프로그래머스 Lv.1 서울에서 김서방 찾기

def solution(seoul):
    for i in range(len(seoul)) :
        if "Kim" == seoul[i] :
            return "김서방은 " + str(i) + "에 있다"