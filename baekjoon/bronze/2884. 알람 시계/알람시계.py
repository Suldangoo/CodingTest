# 2884. 알람 시계 (브론즈 3)
# 알고리즘 분류 : 수학, 사칙연산

h, m = map(int, input().split())

if m - 45 >= 0 : # 45분보다 큰지 조건 체크
    print(h, m - 45)
else :
    if h == 0 : # 0시인지 조건 체크
        print(23, 60 + m - 45)
    else :
        print(h - 1, 60 + m - 45)