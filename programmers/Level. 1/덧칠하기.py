# 프로그래머스 Lv.1 덧칠하기

def solution(n, m, section):
    answer = 0
    
    wall = [True for _ in range(n + 1)] # True로 전부 칠해진 리스트 생성
    
    for i in section :
        wall[i] = False # section 번지를 False로 지우기
        
    # 벽 탐색
    for i in range(n - m + 2) :
        if wall[i] == False : # 비어있는 공간이 있다면
            for j in range(i, i + m) :
                wall[j] = True # m 길이만큼의 공간을 True로 칠하기
            answer += 1 # 한 번 칠함을 체크
            
    # 오른쪽에 칠하지 못한 부분을 체크
    if False in wall[n - m + 2:] :
        # 칠하지 못한 구역이 한 칸이라도 있다면, 한 번 더 칠함
        answer += 1
    
    return answer