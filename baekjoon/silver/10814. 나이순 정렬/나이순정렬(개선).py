# 10814. 나이순 정렬 (실버 5)
# 알고리즘 분류 : 정렬

import sys

n = int(sys.stdin.readline())

nameDict = {} # 키 : 나이 / 값 : 이름 리스트

for _ in range(n) :
    a, b = sys.stdin.readline().rstrip().split()

    # 딕셔너리에 나이와 이름 리스트를 담을 것
    if a not in nameDict : # 만약 해당 나이가 키로 존재하지 않다면
        nameDict[a] = [b] # 이름 리스트 첫 등록
    else : # 해당 나이가 키로 존재한다면
        nameDict[a].append(b) # 이름 리스트에 추가

nameDict = dict(sorted(nameDict.items()))

for k, v in nameDict.items() :
    # v가 빌 때까지 v(이름 리스트)의 가장 왼쪽을 pop하며 출력
    while v :
        print(k, v.pop(0))