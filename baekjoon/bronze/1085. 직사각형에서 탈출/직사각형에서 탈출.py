# 1085. 직사각형에서 탈출 (브론즈3)
# 알고리즘 분류 : 수학, 기하학

# 한수의 위치 좌표와 직사각형의 크기값 입력
x, y, w, h = map(int, input().split())

distances = [x, y, w - x, h - y] # 상하좌우 방향으로 탈출하는 모든 거리를 구함
min_distance = min(distances) # 그중 최솟값을 구함

print(min_distance)