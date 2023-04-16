# 16505. 별 (실버 3)
# 알고리즘 분류 : 구현, 재귀

# 0 일땐 (0,0)
# 1 일땐 (1,0) (0,0) (0,1)
# 2 일땐 (0,3) (0,1) (2,1)

import math

def star (x, y, starList, n) :
    
    
    starList[x][y] = 1

    if n == 0 :
        return

    star(math.trunc(x / 2), y, starList, n - 1)
    star(math.trunc(x / 2), 2 ** n // 2, starList, n - 1)

n = int(input())

# 한 변의 길이가 2^n 인 0으로 가득 찬 2차원 리스트를 생성한다
starList = [[0] * (2 ** n) for _ in range(2 ** n)]



# 프랙탈의 가장 왼쪽 아래 꼭짓점 포인트를 잡는다
x = 2 ** n - 1
y = 0

star(x, y, starList, n)


# # 프랙탈의 왼쪽 위와 오른쪽 위의 꼭짓점 포인트를 잡는다
# x = math.trunc(x / 2)
# starList[x][y] = 1

# y = 2 ** n // 2
# starList[x][y] = 1

# 함수를 작성한다







for i in starList :
    print(i)