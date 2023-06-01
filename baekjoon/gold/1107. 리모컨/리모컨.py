# 1107. 리모컨 (골드 5)
# 알고리즘 분류 : 브루트포스

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
broken = []
if m > 0 :
    broken = list(map(int, sys.stdin.readline().split()))

# 가고자 하는 채널까지 + 혹은 - 만 눌러 가는 값을 가장 디폴트 값으로 선정
result = abs(n - 100)

# 0 ~ 1,000,000 까지의 모든 정수를 브루트포스
# 여기서 최대 채널인 500,000까지가 아닌 1,000,000 까지 브루트포스를 하는 이유는,
# 가고자 하는 채널이 500,000까지이지 채널은 무한대로 존재하기 때문.
# 즉, 500,000번으로 가고 싶지만 3, 4, 5가 고장난 경우에는 299,999번에서 +를 200,001번 누르는 것이 아닌
# 600,000번에서 -를 100,000번 누르는 것이기 때문.
for num in range(1000001) :

    # 고장난 버튼이 하나라도 있다면 해당 채널은 +- 검사가 필요 없으므로 break
    num = str(num)
    for i in range(len(num)) :
        if int(num[i]) in broken :
            break

        # 고장난 버튼이 없었다면, 해당 채널에서 +- 를 눌러 원하는 채널까지 가는 버튼 수를 구함
        # 이후 result와 비교하여, 적다면 result를 교체
        elif i == len(num) - 1 :
            result = min(result, len(num) + abs(n - int(num))) # num 채널을 누르는데 든 횟수와 +- 를 누르는데 든 횟수

print(result)