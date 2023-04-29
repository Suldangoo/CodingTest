# 11047. 동전 0 (실버 4)
# 알고리즘 분류 : 그리디 알고리즘

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = [] # 동전들을 담을 리스트
total = 0 # 필요한 동전의 총 개수

for _ in range(n) :
    coins.append(int(sys.stdin.readline()))

coins = sorted(coins, reverse = True) # 동전을 가치가 큰 동전부터 정렬

for i in coins :
    total += k // i # 동전으로 나눈 몫값을 동전의 개수에 추가
    k %= i # 남은 돈을 반환

print(total)