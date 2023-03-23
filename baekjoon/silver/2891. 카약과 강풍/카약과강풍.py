# 2891. 카약과 강풍 (실버5)
# 알고리즘 분류 : 그리디, 구현

n, s, r = map(int, input().split()) # 팀의 수 / 카약이 손상된 팀의 수 / 카약을 하나 더 가져온 팀의 수 입력받기
damaged = list(map(int, input().split())) # 카약이 손상된 팀의 번호 입력받기
more = list(map(int, input().split())) # 카약을 하나 더 가져온 팀의 번호 입력받기
team = {} # 팀 딕셔너리 생성 (팀 번호 - 1 : 카약의 수)
count = 0 # 출전할 수 없는 팀 변수 생성

# 팀에 카약 채우기 for문
for i in range(n) :
    team[i] = 1 # 우선 모든 팀에 0번부터 시작하여 카약을 하나 준 것으로 시작
    if (i+1) in damaged :
        team[i] -= 1 # 그 팀이 카약이 손상된 팀의 번호에 있다면, 카약을 하나 빼기
    if (i+1) in more :
        team[i] += 1 # 그 팀이 카약을 하나 더 가져온 팀의 번호에 있다면, 카약을 하나 더하기

# 카약 빌려주기 for문
for i in range(0, n) : # 2번 팀 ~ 마지막 - 1 팀까지 반복
    if team[i] == 2 :
        if team[i - 1] == 0 and i != 0 : #  앞 팀에 먼저 카약이 없는지 체크, 해당 팀이 카약이 2개 있어야 성립
            team[i] -= 1
            team[i - 1] += 1
        elif team[i + 1] == 0 and i != (n-1) : # 이후에 뒷 팀에 카약이 없는지 체크
            team[i] -= 1
            team[i + 1] += 1

for k, v in team.items() :
    # 모든 팀의 카약 상황을 출력하고 싶다면 해당 명령어 사용
    # print(k, v)
    if v == 0 : # 출전할 수 없는 팀이 감지될 때마다
        count += 1 # count++

print(count)