# 2675. 숫자의 합 (브론즈 2)
# 알고리즘 분류 : 구현, 문자열

for i in range(int(input())) :
    r, s = input().split()
    r = int(r)

    for j in range(len(s)) :
        print(r * s[j], end = "") # 파이썬의 문자열 * 정수 방식을 사용

    print() # 줄넘김을 해주어야 개행이 되어 다음 입출력에 대해 올바르게 출력됨