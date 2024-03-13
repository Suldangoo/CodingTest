# 프로그래머스 Lv.3 정수 삼각형

def solution(triangle):
    # 삼각형의 위 층 숫자를 아래 층 숫자에 더한 뒤 위 층을 삭제하는 형태
    # 아래 층 숫자에 수를 더할 때, 위 층 중 왼쪽 / 오른쪽 더 큰 수를 더해야 함
    
    for i in range(1, len(triangle)) : # 1부터 삼각형 층수까지 반복
        for j in range(i + 1) : # 0부터 해당 층수의 배열 끝까지 반복
            if j == 0 : # 제일 왼쪽 숫자의 경우 바로 위 층의 가장 왼쪽 숫자를 더함
                triangle[i][j] += triangle[i - 1][0]
            elif j == i : # 제일 오른쪽 숫자의 경우 바로 위층의 가장 오른쪽 숫자를 더함
                triangle[i][j] += triangle[i - 1][-1]
            else : # 그 외의 모든 경우는 위 층의 숫자 두 개중 큰 수를 더함
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
                
    return max(triangle[-1])