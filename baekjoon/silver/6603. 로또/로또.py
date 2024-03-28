# 6603. 로또 (실버 2)
# 알고리즘 분류 : 수학, 조합론, 백트래킹, 재귀, 깊이 우선 탐색

# 현재까지의 조합, 이동 횟수
def dfs(combination, idx) :
    # 현재까지의 조합이 6자리가 되었다면 출력 후 리턴
    if len(combination) == 6 :
        print(" ".join(map(str, combination)))
        return

    # 이동 횟수가 집합의 크기와 같다면 모든 숫자를 확인한 것이므로 리턴
    if idx == k:
        return

    dfs(combination + [lotto[idx]], idx + 1) # 현재 숫자를 포함해서 재귀
    dfs(combination, idx + 1) # 현재 숫자를 포함하지 않고 재귀


while True:
    nums = list(map(int, input().split()))
    k = nums[0] # 집합의 크기를 k에 받음
    if k == 0 : # 리스트의 앞 번호가 0이라면 종료
        break

    lotto = nums[1:] # 크기를 제외한 숫자를 로또라는 이름의 리스트에 설정

    dfs([], 0)
    print()