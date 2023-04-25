# 9657. 돌 게임 3 (실버 3)
# 알고리즘 분류 : 다이나믹 프로그래밍, 게임 이론

n = int(input())
winner = [1, 0, 1, 1]

for i in range(5, 1001) :
    if winner[i - 2] + winner[i - 4] + winner[i - 5] < 3 :
        winner.append(1)
    else :
        winner.append(0)

if winner[n - 1] == 0 :
    print('CY')
else :
    print('SK')