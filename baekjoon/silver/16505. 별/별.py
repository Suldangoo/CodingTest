# 16505. 별 (실버 3)
# 알고리즘 분류 : 구현, 재귀

def star (x, y, point) :
    # 현재 포인트에 별을 찍는다
    starList[x][y] = '*'

    # point가 0에 다다랐다면 재귀함수를 return한다
    if point == 0 :
        return
    
    # point를 절반 줄인다
    next_point = int(point / 2)

    star(x + next_point, y, next_point) # 프랙탈의 밑 프랙탈을 처리하는 재귀
    star(x, y + next_point, next_point) # 프랙탈의 오른쪽 프랙탈을 처리하는 재귀
    star(x, y, next_point) # 현재 기준점의 프랙탈을 처리하는 재귀

n = int(input())

# 한 변의 길이가 2^n 인 빈칸으로 가득 찬 2차원 리스트를 생성한다
starList = [[' '] * (2 ** n) for _ in range(2 ** n)]

point = 2 ** n # 2의 n제곱으로 된 사이즈를 결정짓는다
star(0, 0, point) # 프랙탈의 가장 왼쪽 위를 기준점으로 잡고 재귀한다

for i in starList :
    # 공백을 제거하기 위해 문자열에 추가 후 rstrip()
    result = ""
    for j in i :
        result += j
    print(result.rstrip())