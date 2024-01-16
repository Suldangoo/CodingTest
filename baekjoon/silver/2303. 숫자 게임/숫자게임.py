# 2303. 숫자 게임 (실버 5)
# 알고리즘 분류 : 구현, 브루트포스

import sys
input = sys.stdin.readline

# 5개의 숫자 리스트를 입력받으면 가장 큰 1자리수를 리턴하는 함수
def FindNum(nums) :
    maxNum = 0

    # 브루트포스로 세 개의 숫자 합 중 1의자리가 가장 큰 것을 탐색
    for i in range(5) :
        for j in range(i + 1, 5) :
            for k in range(j + 1, 5) :
                num = (nums[i] + nums[j] + nums[k]) % 10
                maxNum = max(maxNum, num)
    
    # 가장 큰 수를 리턴
    return maxNum

N = int(input())

maxNum = 0 # 지금까지의 수중 가장 큰 수
answer = 0 # 승리자

for i in range(1, N + 1) :
    nums = list(map(int, input().split()))
    num = FindNum(nums)
    if maxNum <= num : # 이상으로 설정하여 승자가 여러명일 경우 이후의 사람이 이기게 됨
        maxNum = num # 값 갱신
        answer = i # 승리자 갱신

print(answer)