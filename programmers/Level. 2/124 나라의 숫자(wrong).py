# 프로그래머스 Lv.2 124 나라의 숫자
# 중복순열로 해결했으며, 시간복잡도가 매우 높은 문제 발생

from itertools import product

def solution(n):
    count = 0
    r = 0
    while True:
        r += 1
        for i in product([1, 2, 4], repeat=r):
            count += 1
            if count == n:
                answer = ''.join(map(str, i))
                return answer