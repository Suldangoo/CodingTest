# 17219. 비밀번호 찾기 (실버 4)
# 알고리즘 분류 : 자료 구조, 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
passwd = dict() # 비밀번호를 저장할 딕셔너리

for _ in range(n) :
    # 사이트 주소와 비밀번호를 저장
    s, p = input().split()
    passwd[s] = p

for _ in range(m) :
    # 입력한 사이트 주소의 비밀번호를 출력
    print(passwd[input().strip()])