# 4779. 칸토어 집합 (실버 3)
# 알고리즘 분류 : 분할 정복, 재귀

# 파일의 입력이 끝날 때 입력이 종료되므로, EOF가 감지되면 입력 종료

while True :
    try :
        # 입력 감지문
        num = int(input())

         # 빈 입력 시 반복문 종료
        if num == '' :
            break

        line = '-' # 빈 줄 추가
        for _ in range(int(num)) : # 입력한 수만큼 반복
            # 라인 + 라인의 길이만큼의 공백 + 라인
            line = line + ' ' * len(line) + line
        print(line)

    except : # EOF 혹은 에러 발생 시 반복문 종료
        break