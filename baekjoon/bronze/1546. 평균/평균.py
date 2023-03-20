# 1546. 평균 (브론즈1)
# 알고리즘 분류 : 수학, 사칙연산

n = int(input())
score = list(map(int, input().split())) # 리스트에 숫자 입력받기
score = sorted(score) # 배열을 정렬

# 첫 번째 부터 마지막까지 원하는 형태로 변환
# 마지막 칸이 가장 큰 점수이므로 별도로 변수를 선언해 줄 필요는 없음
for i in range(n) :
    score[i] = score[i] / score[-1] * 100

print(sum(score) / len(score)) # 평균 출력