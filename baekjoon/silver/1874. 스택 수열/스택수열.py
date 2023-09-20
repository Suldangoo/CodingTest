# 1874. 스택 수열 (실버 2)
# 알고리즘 분류 : 자료 구조, 스택

import sys

n = int(sys.stdin.readline())
nums = []
num = 1 # 1부터 n까지 증가할 수
answer = [] # +와 -가 담길 최종 답 리스트
stack = [] # 풀이에 쓰일 스택 리스트

for _ in range(n) :
    nums.append(int(sys.stdin.readline())) # 사용자로부터 수열을 입력받아 nums에 추가

# 입력한 수열과 숫자 하나씩 비교
for i in nums :
    while i not in stack : # 만약 스택에 수열의 숫자가 업다면
        answer.append('+') # 숫자 팔레트에서 push로 스택에 숫자를 가져오기
        stack.append(num)
        num += 1

    if stack[-1] == i : # 스택의 가장 마지막 수가 수열의 숫자라면
        answer.append('-') # 스택에서 pop으로 숫자 출력
        stack.pop()
    else :
        print("NO") # 아니라면 수열을 완성할 수 없으므로 NO로 종료
        exit(0)

print(*answer, sep='\n') # 정답 문자열을 전부 출력