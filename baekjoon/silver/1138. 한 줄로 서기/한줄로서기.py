# 1138. 한 줄로 서기 (실버 2)
# 알고리즘 분류 : 구현

import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

result = [] # 줄을 서는 번호를 담을 리스트

# 키가 가장 큰 사람부터 줄을 세우기 시작
for i in reversed(p) :
    # 자기보다 키가 큰 사람이 없다면 가장 왼쪽에 세우고
    # 자기보다 키가 큰 사람이 있다면 그 수만큼 오른쪽에 세우기
    result.insert(i, n)
    n -= 1

for i in result :
    print(i, end = ' ')