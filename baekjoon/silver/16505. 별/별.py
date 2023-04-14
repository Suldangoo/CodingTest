# 16505. 별 (실버 3)
# 알고리즘 분류 : 구현, 재귀

n = int(input())

if n == 0 :
    print('*')
else :
    for i in range(1, n + 1) :
        print("**" * i)