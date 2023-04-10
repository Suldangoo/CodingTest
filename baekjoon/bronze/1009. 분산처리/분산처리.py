# 1009. 분산처리 (브론즈 2)
# 알고리즘 분류 : 수학, 구현

# 테스트 케이스의 개수 T를 입력받음
T = int(input())

# T번 반복하면서 각각의 테스트 케이스에 대해 처리된 마지막 데이터의 번호를 출력함
for _ in range(T):
    # 정수 a와 b를 입력받음
    a, b = map(int, input().split())
    # pow(a, b, 10)을 계산하여 처리된 마지막 데이터의 번호를 구함
    last_data = pow(a, b, 10)
    # 처리된 마지막 데이터의 번호가 0일 경우 10번 컴퓨터에 할당됨
    if last_data == 0:
        print(10)
    # 처리된 마지막 데이터의 번호가 0이 아닐 경우 해당 컴퓨터에 할당됨
    else:
        print(last_data)