# 8958. OX퀴즈 (브론즈2)
# 알고리즘 분류 : 구현, 문자열

n = int(input())

for _ in range(n) :
    score = 0 # 총점
    plus = 0 # 1씩 더해지며 가속받을 점수
    ox = input()
    for i in ox : # 문자열을 for문으로 받으면 한 글자씩 들어감
        if i == 'O' :
            plus += 1 # 가속받을 점수에 1점을 더하고
            score += plus # 총점에 더함
        else :
            plus = 0 # X가 나왔다면 plus 변수를 초기화
    print(score)