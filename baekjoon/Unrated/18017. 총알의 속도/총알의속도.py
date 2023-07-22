# 18017. 총알의 속도
# 알고리즘 분류 : 수학, 물리학

# 두 정수를 입력받음
a, b = map(float, input().split())

# 뉴턴의 물리법칙이 아닌 상대성 이론에 의거하여 속도 공식 작성
light = 299792458
speed = (a + b) / (1 + (a * b) / (light * light))
print("%.2f" % speed)