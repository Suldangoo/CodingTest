# 1436. 영화감독 숌 (실버 5)
# 알고리즘 분류 : 브루트포스

import sys
n = int(sys.stdin.readline())

cnt = 1 # 지금이 몇 번째 666 수인지 체크할 변수
num = 666 # 666부터 시작해 숫자를 하나씩 올릴 변수

# cnt가 입력한 값이 될 때까지 반복
while(cnt < n) :
    num += 1 # 수 증가
    if '666' in str(num) : # 해당 수에 666이 있다면
        cnt += 1 # cnt 1개 증가

print(num)