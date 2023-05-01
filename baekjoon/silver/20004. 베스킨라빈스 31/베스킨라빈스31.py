# 20004. 베스킨라빈스 31 (실버 4)
# 알고리즘 분류 : 수학, 게임 이론

A = int(input())

# 1부터 입력한 수까지 반복
for i in range(1, A + 1) :
    num = 30 # 30을 말하면 승리하므로, 30을 선점할 수 있는지 확인
    while True :
        # 0이 되지 않을 때까지 확인할 수 + 1 만큼 빼기
        if num - (i + 1) > 0 :
            num -= (i + 1)
        else :
            break

    # 해당 수를 상대가 말할 수 없다면 자신의 승리
    if i < num :
        print(i)