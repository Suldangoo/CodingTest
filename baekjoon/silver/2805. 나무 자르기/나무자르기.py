# 2805. 나무 자르기 (실버 2)
# 알고리즘 분류 : 이진 탐색, 매개 변수 탐색

import sys
input = sys.stdin.readline

# 필요값을 입력받음
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 1 ~ 나무의 최대 값까지를 범위로 잡아냄
start = 1
end = max(trees)

while start <= end :
    # 이진 탐색
    middle = (start + end) // 2
    cut = 0

    # 만약 나무의 크기가 가운뎃값보다 크다면, 잘라서 저장
    for tree in trees :
        if tree > middle :
            cut += tree - middle
    
    # 모은 양이 충분하다면 높이를 높인다
    if cut >= M :
        start = middle + 1
    # 모은 양이 부족하다면 높이를 낮춘다
    else :
        end = middle - 1

# 적어도 M미터 이상의 나무를 챙겨야하므로 end 출력
print(end)