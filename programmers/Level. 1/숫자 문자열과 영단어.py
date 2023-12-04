# 프로그래머스 Lv.1 숫자 문자열과 영단어
# 2021 카카오 채용연계형 인턴십

def solution(s):
    
    temp = ""
    answer = ""
    
    for i in s :
        if i.isdecimal() :
            answer += i
        else :
            temp += i
        
        if temp == "zero" :
            answer += "0"
            temp = ""
        elif temp == "one" :
            answer += "1"
            temp = ""
        elif temp == "two" :
            answer += "2"
            temp = ""
        elif temp == "three" :
            answer += "3"
            temp = ""
        elif temp == "four" :
            answer += "4"
            temp = ""
        elif temp == "five" :
            answer += "5"
            temp = ""
        elif temp == "six" :
            answer += "6"
            temp = ""
        elif temp == "seven" :
            answer += "7"
            temp = ""
        elif temp == "eight" :
            answer += "8"
            temp = ""
        elif temp == "nine" :
            answer += "9"
            temp = ""
    
    return eval(answer)