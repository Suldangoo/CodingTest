# 3024. 마라톤 틱택토 (실버 3)
# 알고리즘 분류 : 브루트포스 알고리즘, 구현

import sys
input = sys.stdin.readline

def Check(n, board) :
    # 가로줄 파악
    for i in range(n) :
        for j in range(n - 2) : # 3개를 파악할 것이므로 n-2까지만 반복
            if board[i][j] != '.' : # 만약 '.'이 들어간 연속 문자열이 아니라면
                if board[i][j] == board[i][j + 1] == board[i][j + 2] : # 3개의 연속된 가로 문자열들이 모두 같은지 확인
                    return board[i][j] # 같다면 해당 문자열 리턴

    # 세로줄 파악
    for i in range(n - 2) : # 3개를 파악할 것이므로 n-2까지만 반복
        for j in range(n) :
            if board[i][j] != '.' : # 만약 '.'이 들어간 연속 문자열이 아니라면
                if board[i][j] == board[i + 1][j] == board[i + 2][j] : # 3개의 연속된 세로 문자열들이 모두 같은지 확인
                    return board[i][j] # 같다면 해당 문자열 리턴
            
    # 오른아래 대각선 파악
    for i in range(n - 2) : # 3개를 파악할 것이므로 n-2까지만 반복
        for j in range(n - 2) :
            if board[i][j] != '.' : # 만약 '.'이 들어간 연속 문자열이 아니라면
                if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] : # 대각선 문자열들이 모두 같은지 확인
                    return board[i][j] # 같다면 해당 문자열 리턴
    
    # 왼아래 대각선 파악
    for i in range(n - 2) : # 3개를 파악할 것이므로 n-2까지만 반복
        for j in range(n - 2) :
            if board[i][n - j - 1] != '.' : # 만약 '.'이 들어간 연속 문자열이 아니라면
                if board[i][n - j - 1] == board[i + 1][n - (j + 1) - 1] == board[i + 2][n - (j + 2) - 1] : # 대각선 문자열들이 모두 같은지 확인
                    return board[i][n - j - 1] # 같다면 해당 문자열 리턴
    
    # 아무런 조건도 만족하지 못했다면 ongoing 출력
    return "ongoing"

N = int(input())

board = []

for _ in range(N) :
    board.append(input().rstrip())

print(Check(N, board))