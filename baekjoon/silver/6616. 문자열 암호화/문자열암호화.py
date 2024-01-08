# 6616. 문자열 암호화 (실버 3)
# 알고리즘 분류 : 문자열, 구현

import sys
input = sys.stdin.readline

while(True) :

    N = int(input()) # 번지수를 점프할 숫자

    # 0 입력 시 반복문 종료
    if (N <= 0) :
        break

    text = input().rstrip() # 문자열 입력받기
    text = text.replace(" " , "") # 공백 완전 제거
    text = text.upper() # 모든 문자열을 대문자로 변환

    start = 0 # 루프를 돌 때 맨 처음 위치를 참조할 변수
    point = 0 # 문자를 삽입할 번지
    size = len(text) # 문자열의 길이

    answer = ['' for _ in range(size)] # 문자열 길이만큼의 번지를 지닌 리스트 생성

    
    for i in text :
        answer[point] = i

        point += N # N만큼 번지수를 점프

        # 만약 문자열의 끝에 도달했다면
        if point >= size :
            start += 1 # 시작 번지수를 1 증가
            point = start # point를 start로 초기화

    print(''.join(answer)) # 리스트에 쌓인 문자열들을 모아 출력