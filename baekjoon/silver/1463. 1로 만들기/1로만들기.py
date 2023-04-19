# 1463. 1로 만들기 (실버 3)
# 알고리즘 분류 : 다이나믹 프로그래밍

n = int(input())

# 원하는 값보다 한 칸 더 많은 리스트 생성
nums = [0 for _ in range(n + 1)]

# 입력한 값 - 1 부터 1까지 역순으로 진행
for i in range(n - 1, 0, -1):
    numList = []

    if i * 3 <= n:
        numList.append(nums[i * 3] + 1) # 현재 값 * 3 을 만드는데 걸린 횟수 추가
    if i * 2 <= n:
        numList.append(nums[i * 2] + 1) # 현재 값 * 2 을 만드는데 걸린 횟수 추가
    numList.append(nums[i + 1] + 1) # 현재 값 + 1 을 만드는데 걸린 횟수 추가

    nums[i] = min(numList) # 그 중 가장 작은 횟수가 현재 값을 만드는 최소 횟수

print(nums[1]) # 1을 만드는 데 가장 작은 횟수 출력