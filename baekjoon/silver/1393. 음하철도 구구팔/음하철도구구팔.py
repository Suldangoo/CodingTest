# 1393. 음하철도 구구팔 (실버 1)
# 알고리즘 분류 : 수학, 브루트포스 알고리즘

import sys
import math

# 최대 공약수를 구하는 함수
def get_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

# 두 점 사이의 거리를 구하는 함수
def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# 시작점의 좌표
start_x, start_y = map(int, sys.stdin.readline().split())

# 도착점과 이동 거리를 입력받음
end_x, end_y, move_x, move_y = map(int, sys.stdin.readline().split())

# 이동 거리의 최대 공약수를 구함
gcd = get_gcd(move_x, move_y)
move_x, move_y = move_x // gcd, move_y // gcd

# 현재 위치를 도착점으로 초기화
current_x, current_y = end_x, end_y

# 현재 위치에서 (move_x, move_y)만큼 이동할 때 다음 지점까지의 거리가 현재 위치에서 도착점까지의 거리보다 작을 때까지 이동
while get_distance(current_x, current_y, start_x, start_y) > get_distance(current_x + move_x, current_y + move_y, start_x, start_y):
    current_x += move_x
    current_y += move_y

# 도착점에서 (move_x, move_y)만큼 이동하면 시작점에 도착하므로 도착점에서 이동한 위치를 출력
print(current_x, current_y)