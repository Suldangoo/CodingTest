# 1515. 수 이어 쓰기 (실버 3)
# 알고리즘 분류 : 구현, 그리디 알고리즘, 문자열, 브루트포스

import sys
input = sys.stdin.readline

nums = input().rstrip()

i = 0 # 1부터 하나씩 증가하는 자연수

while len(nums) > 0 : # nums 문자열이 모두 소모될 때까지 반복
    i += 1 # i 수 증가
    num = str(i) # 현재 수 체크

    # num 문자열이 존재하며, nums 문자열이 존재하다면 반복
    while len(num) > 0 and len(nums) > 0 :
        if nums[0] == num[0] : # nums의 맨 앞에 원하는 수가 있다면
            nums = nums[1:] # nums 앞 숫자를 제거
        num = num[1:] # 없다면 num 앞 숫자를 제거

# 반복문이 끝났다면 nums를 모두 체크한 것이므로, num 출력
print(i)