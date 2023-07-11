# 10162. 전자레인지 (브론즈 3)
# 알고리즘 분류 : 그리디, 구현, 수학

t = int(input()) # 전자레인지에 돌릴 시간을 초단위로 입력받음
button_dict = {300 : 0, 60 : 0, 10 : 0} # 3개의 버튼과 각각 몇 번 눌렸는지 체크할 딕셔너리 생성

if (t % 10 == 0) : # 10으로 나누어 떨어지지 않을 경우 -1 출력
    for k, v in button_dict.items() : # 딕셔너리의 items를 k와 v에 넣어 반복문 시작
        button_dict[k] += t // k # 딕셔너리의 값에 시간을 버튼의 단위로 나눈 몫을 더함
        t %= k # 계산 후 남은 시간에 반환
    print(button_dict[300], button_dict[60], button_dict[10]) # 결과 출력, for안에 넣지 않아서 시간을 단축
else :
    print(-1)