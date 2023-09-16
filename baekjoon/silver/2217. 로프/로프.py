# 2217. 로프 (실버 4)
# 알고리즘 분류 : 수학, 그리디 알고리즘, 정렬

N = int(input())
nums = []

# nums 리스트에 숫자를 N개 입력받음
for _ in range(N) :
    nums.append(int(input()))

# 역순으로 정렬
nums = sorted(nums, reverse=True)
max = nums[0] # 로프들을 여러개 사용하여 들 수 있는 가장 큰 무게

for i in range(1, N) :
    # 무거운 것을 들 수 있는 로프들 순서대로 하나씩 더 사용 후 비교
    if nums[i] * (i + 1) > max :
        max = nums[i] * (i + 1)

print(max)