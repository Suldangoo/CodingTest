# 2562. 최댓값 (브론즈 3)
# 알고리즘 분류 : 구현

n = int(input())
top = n # 첫 번째 값은 그냥 입력받은 후 top 변수에 저장
num = 1 # 첫 번째 값이 가장 큰 번호라고 가정

for i in range(8) : # 이후 8번 더 입력받음
    n = int(input())
    if top < n : # 만약 n이 top보다 더 크다면, 새로운 최댓값 등장
        # 변수 갱신
        top = n
        num = i + 2

print(top)
print(num)