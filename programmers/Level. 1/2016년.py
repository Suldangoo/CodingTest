# 프로그래머스 Lv.1 2016년

def solution(a, b):
    date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 1월 ~ 12월까지의 일 수
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'] # 일 ~ 토요일까지의 문자열 리스트
    # 1월 1일이 금요일이기 때문에, day값이 1일 때 FRI가 나오도록 배열 조정
    
    day = 0 # 총 일수의 합
    
    for i in range(a - 1) :
        day += date[i] # 현재까지 월들의 모든 일수 더하기
    day += b # 현재 일수 더하기
    day %= 7 # 7로 나눈 나머지 값을 구해서 기준값 생성
    
    return week[day]