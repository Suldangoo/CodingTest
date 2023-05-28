# 12101. 1, 2, 3 더하기 2 (실버 1)
# 알고리즘 분류 : 브루트포스 알고리즘, 백트래킹

def dfs(nums, accumulate, target):
    # 타겟의 숫자를 만들기 위해 nums에 1, 2, 3을 넣으며 재귀를 돌림
    global case # 전역변수 리스트 case를 사용

    # 현재 누적값이 목표치와 같으면 리스트 추가 후 리턴
    if accumulate == target:
        case.append(nums)
        return
    
    # 현재 누적값이 목표치를 넘겨버렸다면 리턴
    if accumulate > target:
        return

    # 1, 2, 3을 넣은 리스트를 생성함과 동시에 누적값을 다음 재귀로 보냄
    # 1 - 1 - 1... 순서부터 시작하므로 정렬해줄 필요가 없음
    for i in [1, 2, 3]:
        dfs(nums + [i], accumulate + i, target)

n, k = map(int, input().split())
case = []

dfs([], 0, n)

# k - 1번째 인덱스 호출
if k - 1 < len(case):
    print("+".join(map(str, case[k - 1])))
else:
    print(-1)