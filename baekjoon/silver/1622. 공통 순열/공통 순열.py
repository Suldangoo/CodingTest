# 1622. 공통 순열 (실버 4)
# 알고리즘 분류 : 문자열, 정렬

# 종료 조건을 위해  try문 사용
try :
    while True :
        answer = list()
        a = input()
        b = input()

        for i in a :
            if i in b : # 문자열 하나가 해당 문자열 안에 존재할 경우
                answer += [i] # 답 리스트에 문자열 추가
                b = b.replace(i, '', 1) # b 문자열에 남은 i들을 모두 제거

        answer = sorted(answer)
        print(''.join(answer))
except :
    pass