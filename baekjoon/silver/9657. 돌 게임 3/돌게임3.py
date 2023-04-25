# 9657. 돌 게임 3 (실버 3)
# 알고리즘 분류 : 다이나믹 프로그래밍, 게임 이론

n = int(input())
# 상근이가 이기는 경우 1
# 찬영이가 이기는 경우 0
winner = [1, 0, 1, 1]

for i in range(5, 1001) :
    # 돌의 개수보다 1개, 3개, 4개 적은 걸 모두 이겼었다면, 해당 돌의 개수는 상대방이 무조건 이김
    if winner[i - 2] + winner[i - 4] + winner[i - 5] < 3 :
        winner.append(1)
    else :
        winner.append(0)

if winner[n - 1] == 0 :
    print('CY')
else :
    print('SK')