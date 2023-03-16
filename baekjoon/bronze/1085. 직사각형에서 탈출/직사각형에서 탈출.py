# 1085. 직사각형에서 탈출 (브론즈3)
# 알고리즘 분류 : 수학, 기하학

# 4개의 정수로 이루어진 좌표값을 입력
x, y, w, h = map(int, input().split())

distances = [x, y, w - x, h - y] # 리스트에 등장 가능한 4가지 경우의 선분 길이를 저장
min_distance = min(distances) # 그 중 최솟값을 찾음

print(min_distance)
