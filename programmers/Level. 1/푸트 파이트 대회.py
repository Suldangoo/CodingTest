# 프로그래머스 Lv.1 푸드 파이트 대회

def solution(food):
    answer = "0"
    food = list(reversed(food))[:-1] # 순서를 뒤집고 물을 빼는 전처리 과정
    num = len(food) # 가장 마지막 음식의 번호
    
    # 물을 제외한 음식부터 루프 시작
    for i in food :
        # 답 = 음식 수의 절반만큼 숫자 + 기존 답 + 음식 수의 절반만큼 숫자
        answer = str(num) * int(i / 2) + answer + str(num) * int(i / 2)
        num -= 1 # 마지막 음식 번호 감소
    
    return answer