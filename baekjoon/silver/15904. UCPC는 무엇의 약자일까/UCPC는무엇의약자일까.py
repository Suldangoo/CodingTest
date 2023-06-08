# 15904. UCPC는 무엇의 약자일까? (실버 5)
# 알고리즘 분류 : 문자열, 그리디 알고리즘

check = 0 # 약자가 맞아떨어질 때마다 증가시켜줄 변수

for i in input() :
    # U - C - P - C 순서대로 맞아떨어지면 check를 증가
    if i == 'U' and check == 0 :
        check += 1
    elif i == 'C' and (check == 1 or check == 3) :
        check += 1
    elif i == 'P' and check == 2 :
        check += 1

if check == 4 :
    # check가 딱 4로 떨어진다면 UCPC로 축약되는 것임
    print("I love UCPC")
else :
    print("I hate UCPC")