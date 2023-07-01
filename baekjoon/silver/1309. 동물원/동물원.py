# 1309. 동물원 (실버 1)
# 알고리즘 분류 : 다이나믹 프로그래밍

N = int(input())

if N == 1 : # 1을 입력한 경우의 예외 처리
    print(3)
else :
    # N 만큼의 길이의 리스트 작성
    dp = [0 for i in range(N + 1)]
    dp[1] = 3
    dp[2] = 7

    # 1과 2일 때의 값을 구해놓은 후 점화식 작성
    for i in range(3, N + 1) :
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901

    print(dp[N])