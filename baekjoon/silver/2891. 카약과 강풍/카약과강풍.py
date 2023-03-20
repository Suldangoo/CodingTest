# 2891. 카약과 강풍 (실버5)
# 알고리즘 분류 : 그리디, 구현

n, s, r = map(int, input().split())
damaged = list(map(int, input().split()))
more = list(map(int, input().split()))
team = {}
count = 0

for i in range(n) :
    team[i] = 1
    if (i+1) in damaged :
        team[i] -= 1
    if (i+1) in more :
        team[i] += 1

if team[0] == 2 and team[1] == 0 :
    team[0] -= 1
    team[1] += 1

if team[n-1] == 2 and team[n-2] == 0 :
    team[n-1] -= 1
    team[n-2] += 1

for i in range(1, n-1) :
    if team[i] == 2 and team[i - 1] == 0 :
        team[i] -= 1
        team[i - 1] += 1
    elif team[i] == 2 and team[i + 1] == 0 :
        team[i] -= 1
        team[i + 1] += 1

for k, v in team.items() :
    # print(k, v)
    if v == 0 :
        count += 1

print(count)