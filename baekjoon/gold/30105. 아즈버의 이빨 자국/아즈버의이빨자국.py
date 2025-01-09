N = int(input()) # 이빨 개수 n
numList = list(map(int, input().split())) # 이빨이 물린 구멍의 위치

# 아즈버의 송곳니 사이 간격은 일정하다.
# 각 구멍들의 위치를 파악하여, 아즈버의 송곳니 간격이 될 수 있는 경우를 구하라.

# TODO : n개의 이빨 개수가 있을 때, 가능한 송곳니 간격은 정해져있다.
# 예를 들어 n이 4와 5일 때는 송곳니 간격이 최대 2이다. 6과 7일 땐 간격이 최대 3이다.

numDict = dict()
answer = []

for i in range(N) :
    numDict[numList[i]] = 1

for i in range(1, N):
    interval = numList[i] - numList[0] # 이번 간격에서 가능한 아즈버의 송곳니 간격

    valid = False

    for j in range(1, N): # 최대한 진행하는 단계
        if numDict.get(numList[j] + interval, 0) == 0 :
            if numDict.get(numList[j] - interval, 0) == 0 :
                valid = True
                break
            
    if valid == False:
        answer.append(interval)

print(len(answer)) # 가능한 아즈버의 송곳니 간격 개수
if len(answer) > 0:
    print(*answer) # 가능한 아즈버의 송곳니 간격을 오름차순으로 정렬