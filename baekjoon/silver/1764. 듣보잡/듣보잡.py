# 1764. 듣보잡 (실버 4)
# 알고리즘 분류 : 자료 구조, 문자열, 정렬

import sys

n, m = map(int, sys.stdin.readline().split())

nameDict = {} # 듣도 못한 사람의 이름을 담을 해시 (딕셔너리)
nameList = [] # 듣도 보도 못한 사람들의 이름을 담을 리스트

for i in range(n):
    name = sys.stdin.readline().strip()
    nameDict[name] = 1 # 해시에 듣도 못한 사람의 이름을 할당

for i in range(m):
    name = sys.stdin.readline().strip()

    # 해시(딕셔너리) 안에서 in으로 원하는 key를 찾는 데에 걸리는 시간 복잡도는 O(1)
    if name in nameDict:
        nameList.append(name)

# 사전순 정렬
nameList.sort()

print(len(nameList))
for name in nameList:
    print(name)