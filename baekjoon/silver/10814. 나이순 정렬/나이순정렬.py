# 10814. 나이순 정렬 (실버 5)
# 알고리즘 분류 : 정렬

import sys

n = int(sys.stdin.readline())

ageList = [] # 모든 나이를 담을 리스트
nameDict = {} # 키 : 나이 / 값 : 이름 리스트

for _ in range(n) :
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a) # 나이는 정수로 반환

    ageList.append(a) # 나이 리스트에 나이를 담음

    # 딕셔너리에 나이와 이름 리스트를 담을 것
    if a not in nameDict : # 만약 해당 나이가 키로 존재하지 않다면
        nameDict[a] = [b] # 이름 리스트 첫 등록
    else : # 해당 나이가 키로 존재한다면
        nameDict[a].append(b) # 이름 리스트에 추가

ageList.sort() # 나이 리스트 정렬

for i in ageList :
    # 나이 출력, 해당 나이 키의 리스트 가장 왼쪽 pop하며 출력
    print(i, nameDict[i].pop(0))