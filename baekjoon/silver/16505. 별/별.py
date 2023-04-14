# 16505. 별 (실버 3)
# 알고리즘 분류 : 구현, 재귀

def star(n):
    if n == 0:
        return ['*']
    stars = star(n-1)
    return stars + [s + ' ' * 2**(n-1) + s for s in stars] + [s * 2 for s in stars]