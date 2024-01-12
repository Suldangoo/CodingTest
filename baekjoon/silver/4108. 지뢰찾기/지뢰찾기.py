# 4108. 지뢰찾기 (실버 5)
# 알고리즘 분류 : 구현

import sys
input = sys.stdin.readline

while(True) :
    r, c = map(int, input().split())

    # 0 0이 입력된다면 프로그램 종료
    if r == c == 0 :
        break

    table = list()
    dx = [0, 0, -1, 1, -1, -1, 1, 1] # 인접 8방향의 좌표차이
    dy = [-1, 1, 0, 0, -1, 1, -1, 1]

    for _ in range(r) :
        # 테이블 입력받기. 단, 한줄한줄을 모두 리스트로 전환 후 추가
        table.append(list(input().rstrip()))

    for x in range(r) : # 모든 r 탐색
        for y in range(c) : # 모든 c 탐색
            if table[x][y] == '.' : # 탐색하는 좌표값이 '.'이라면
                table[x][y] = 0 # 해당 좌표값을 int형의 0으로 교체
                for i in range(8) : # 인접한 8칸을 모두 탐색
                    a = x + dx[i]
                    b = y + dy[i]
                    if a >= 0 and a < r and b >= 0 and b < c : # 설정한 좌표값이 테이블 영역 바깥이 아니라면
                        if table[a][b] == '*' : # 탐색하는 좌표에 있는 것이 지뢰라면
                            table[x][y] += 1 # 숫자 1 증가
                table[x][y] = str(table[x][y]) # 인접 지뢰 개수 파악 후 str로 교체

    for i in table :
        print(''.join(i))