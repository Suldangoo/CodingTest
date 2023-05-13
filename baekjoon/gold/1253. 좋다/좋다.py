# 1253. 좋다 (골드 4)
# 알고리즘 분류 : 자료 구조, 정렬, 이분 탐색, 두 포인터

import sys

if __name__ == '__main__':
    # 입력 받기
    N = int(input()) # 배열의 요소 개수
    arr = list(map(int, sys.stdin.readline().split())) # 배열의 요소들

# 배열 정렬
arr.sort()
ans = 0  # 정답 카운트 초기화

# 배열의 각 요소에 대해 반복
for i in range(N):
    # 현재 요소를 배열에서 제외한 새로운 배열 생성
    tmp = arr[:i] + arr[i + 1:]
    left, right = 0, len(tmp) - 1  # 두 요소 합을 찾기 위한 포인터 초기화

    # 두 요소 합을 찾는 과정
    while left < right:
        t = tmp[left] + tmp[right]  # 두 요소의 합 계산

        if t == arr[i]:
            ans += 1  # 합이 제외된 요소와 같으면 정답 카운트 증가
            break

        if t < arr[i]:
            left += 1  # 합이 작으면 왼쪽 포인터 증가
        else:
            right -= 1  # 합이 크면 오른쪽 포인터 감소

print(ans)  # 최종 정답 카운트 출력