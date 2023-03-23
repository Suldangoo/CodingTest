# 3052. 나머지 (브론즈 2)
# 알고리즘 분류 : 수학, 사칙연산

# 중복을 제거하기 위한 빈 set 생성
nums = set()

for _ in range(10) : 
    num = int(input()) % 42 # 입력받은 값에 42를 나눈 나머지를 저장
    nums.add(num) # set에 add

print(len(nums)) # set의 길이 출력