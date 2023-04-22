# 11866. 요세푸스 문제 0 (실버 5)
# 알고리즘 분류 : 구현, 자료 구조, 큐

import sys
n, k = map(int, sys.stdin.readline().split())

# 1번부터 시작하는 숫자들의 리스트 생성
nums = [i for i in range(1, n + 1)]
result = [] # 출력되는 답을 담을 리스트

start = 0
while nums:
    end = (start + k - 1) % len(nums) # 포인터를 오른쪽으로 이동시키며 nums의 길이를 넘지 않을 것
    result.append(nums.pop(end)) # 포인터의 숫자를 리스트에 추가
    start = end # 시작점을 현재 점으로 설정

print('<', end='')
print(*result, sep=', ', end='') # 리스트의 모든 내용 출력, 구분자를 ', ' 로 설정
print('>')