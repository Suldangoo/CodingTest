# 3663. 고득점 (골드 3)
# 알고리즘 분류 : 그리디 알고리즘, 브루트포스 알고리즘

def check(nums, a, b, c) :
    num = 0
    for i in range(a, b, c) :
        num += nums[i]
        nums[i] = 0
        
        if sum(nums) == 0 :
            break
        
        num += 1
    return num

N = int(input())
for i in range(N) :
    name = input()

    nums = []
    for i in name :
        if ord(i) - 65 < 26 - (ord(i) - 65) :
            nums.append(ord(i) - 65)
        else :
            nums.append(26 - (ord(i) - 65))
    print(min(check(nums.copy(), 0, len(nums), 1), check(nums, 0, 0 - len(nums), -1)))