# 2798. 블랙잭 (브론즈 2)
# 알고리즘 분류 : 브루트포스 알고리즘

N, M = map(int, input().split()) # N, M 입력받기
cards = list(map(int, input().split())) # 카드에 쓰여있는 수 입력받기

max_sum = 0 # 가능한 모든 3장의 합 중 최대값
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            # i, j, k 인덱스에 해당하는 카드 3장의 합 계산
            current_sum = cards[i] + cards[j] + cards[k]
            if current_sum <= M: # 합이 M 이하이면서
                max_sum = max(max_sum, current_sum) # 최대값 갱신

print(max_sum) # 결과 출력