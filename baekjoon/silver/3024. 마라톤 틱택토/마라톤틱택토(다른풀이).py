# 3024. 마라톤 틱택토 (실버 3)
# 알고리즘 분류 : 브루트포스 알고리즘, 구현

# 똑같은 글자가 세 번 연속이 아닌 한 행 / 한 열 / 대각선을 모두 차지하고 있어야 승리하는 코드

import sys
input = sys.stdin.readline

def Check(n, board) :
    # 가로줄 파악
    for i in range(n) :
        char = board[i][0] # 첫 문자열 확인
        for j in range(1, n) :
            # 만약 문자열이 다르다면, 즉시 다음 가로줄로 이동
            if char != board[i][j] :
                break
            # 만약 끝까지 같은 문자열로 도달했으며, '.'이 아니라면
            if j + 1 == n and char != '.' :
                return char

    # 세로줄 파악
    for i in range(n) :
        char = board[0][i] # 첫 문자열 확인
        for j in range(1, n) :
            # 만약 문자열이 다르다면, 즉시 다음 세로줄로 이동
            if char != board[j][i] :
                break
            # 만약 끝까지 같은 문자열로 도달했다면
            if j + 1 == n and char != '.' :
                return char
            
    # 대각선줄 파악 (오른쪽 아래로)
    char = board[0][0] # 첫 문자열 확인
    for i in range(1, n) :
        # 만약 문자열이 다르다면, 반복문 종료
        if char != board[i][i] :
            break
        # 만약 끝까지 같은 문자열로 도달했다면
        if i + 1 == n and char != '.' :
            return char
    
    # 대각선줄 파악 (왼쪽 아래로)
    char = board[0][n - 1] # 첫 문자열 확인
    for i in range(1, n) :
        # 만약 문자열이 다르다면, 반복문 종료
        if char != board[i][n - (i + 1)] :
            break
        # 만약 끝까지 같은 문자열로 도달했다면
        if i + 1 == n and char != '.' :
            return char
    
    # 아무런 조건도 만족하지 못했다면 ongoing 출력
    return "ongoing"

N = int(input())

board = []

for _ in range(N) :
    board.append(input().rstrip())

print(Check(N, board))