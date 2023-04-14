# 4153. 직각삼각형 (브론즈 3)
# 알고리즘 분류 : 수학, 기하학, 피타고라스의 정리

import sys

while True :
    nums = list(map(int, sys.stdin.readline().split()))
    if sum(nums) == 0 :
        break
    else :
        nums = sorted(nums)
        if pow(nums[0], 2) + pow(nums[1], 2) == pow(nums[2], 2) :
            print("right")
        else :
            print("wrong")