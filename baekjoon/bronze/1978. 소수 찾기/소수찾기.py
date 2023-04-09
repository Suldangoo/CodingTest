# 1978. 소수 찾기 (브론즈 2)
# 알고리즘 분류 : 소수 판별, 수학, 정수론

n = int(input()) # 수의 개수 입력
numbers = list(map(int, input().split())) # N개의 수 입력받아 리스트로 저장

count = 0 # 소수의 개수를 저장할 변수

for num in numbers:
    if num == 1: # 1은 소수가 아님
        continue
    for i in range(2, int(num ** 0.5) + 1): # 2부터 해당 수의 제곱근까지 나누어 떨어지는지 검사
        if num % i == 0:
            break # 나누어 떨어지면 소수가 아님
    else:
        count += 1 # 나누어 떨어지지 않으면 소수이므로 count를 1 증가

print(count) # 소수의 개수 출력