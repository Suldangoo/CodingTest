# 3663. 고득점 (골드 3)
# 알고리즘 분류 : 그리디 알고리즘, 브루트포스 알고리즘

def solution(name):
    answer = 0
    length = len(name)

    # 알파벳을 만드는 데 필요한 조이스틱 클릭 횟수
    for letter in name:
        answer += min(ord(letter) - ord('A'), abs(ord(letter) - ord('Z') - 1))

    # 모든 자리를 움직였을 때 최소 자리
    min_move = length - 1
    for i in range(length):
        next_i = i + 1
        # 왼쪽 -> 오른쪽 이동 혹은 오른쪽 -> 왼쪽 이동
        while next_i < length and name[next_i] == 'A':
            next_i += 1

        # 더 적은 것으로 골라 선택
        min_move = min(min_move, i + (i + length - next_i), 2 * (length - next_i) + i)

    answer += min_move
    return answer


T = int(input())
for _ in range(T):
    print(solution(input()))