# 12865. 평범한 배낭 (골드5)
# 알고리즘 분류 : 다이나믹 프로그래밍, Knapsack problem

n, k = map(int, input().split()) # 물품의 수 n과 버틸 수 있는 무게 k 입력받기
dp = [0] * (k+1) # dp 테이블 초기화

for i in range(n):
    w, v = map(int, input().split()) # 각 물건의 무게 w와 가치 v 입력받기
    for j in range(k, w-1, -1):
        # 현재 물건의 무게부터 시작해서 역순으로 탐색하며 dp 테이블 갱신
        # j는 현재 배낭에 넣을 수 있는 무게를 의미
        # w보다 작은 무게는 배낭에 넣을 수 없으므로 무시한다
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[k]) # 배낭에 넣을 수 있는 물건들의 가치합의 최댓값 출력