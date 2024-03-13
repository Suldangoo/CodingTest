# 2992. 크면서 작은 수 (실버 3)
# 알고리즘 분류 : 브루트포스 알고리즘, 백트래킹

from itertools import permutations

# 튜플을 숫자로 변환하는 함수
def tuple_to_int(t):
    return int(''.join(t))

x = input() # 숫자를 입력받되, 문자열의 형태로 입력받음
perms = permutations(x, len(x)) # 해당 숫자들로 만들 수 있는 순열 생성

nums = list(map(tuple_to_int, perms)) # 각 순열을 숫자로 변환
nums = sorted(nums) # 숫자를 정렬

# 리스트를 탐색하며 기초 수보다 큰 수가 나오면 즉시 출력 후 프로그램 종료
for i in nums :
    if i > int(x) :
        print(i)
        exit(0)

# 끝까지 출력되지 않았다면 0 출력
print(0)