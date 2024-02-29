# 1622. 공통 순열 (실버 4)
# 알고리즘 분류 : 문자열, 정렬

try :
    while True :
        answer = set()
        a = input()
        b = input()

        for i in a :
            if i in b :
                answer.add(i)

        answer = sorted(list(answer))
        print(''.join(answer))
except :
    pass