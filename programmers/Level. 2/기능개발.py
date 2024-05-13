# 프로그래머스 Lv.2 기능 개발

def solution(progresses, speeds):
    answer = [] # 정답 리스트
    
    # 작업 리스트가 채워져있을 경우 반복
    while progresses :
        progresses = [x + y for x, y in zip(progresses, speeds)] # 두 리스트를 합함
        
        # 맨 앞 작업이 완료되었을 경우
        if progresses[0] >= 100 :
            answer.append(0) # answer 변수 추가
            while progresses and progresses[0] >= 100 : # 작업 리스트가 채워져있고, 맨 앞 작업이 완료된 이상 반복
                answer[-1] += 1
                progresses.pop(0) # 맨 앞 작업 제거
                speeds.pop(0) # 해당 작업의 속도 리스트도 한 칸 제거
    
    return answer