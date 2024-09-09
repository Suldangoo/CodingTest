# PCCP 기출문제 1번
# 프로그래머스 Lv.1 동영상 재생기

def timeconvert(time) :
    m, s = map(int, time.split(':')) # :를 기준으로 분과 초로 분할
    
    return m * 60 + s # 초로 환산

def timeskip(time, op_start, op_end) :
    if time in range(op_start, op_end + 1) :
        time = op_end # 오프닝 시간 사이일 경우 시간을 오프닝 끝으로 설정
        
    return time

def solution(video_len, pos, op_start, op_end, commands) :
    pos = timeskip(timeconvert(pos), timeconvert(op_start), timeconvert(op_end)) # 우선 오프닝 스킵 작업
    
    for i in commands :
        if i == "prev" :
            pos -= 10
            pos = max(pos, 0)
        elif i == "next" :
            pos += 10
            pos = min(pos, timeconvert(video_len))
            
        pos = timeskip(pos, timeconvert(op_start), timeconvert(op_end)) # 이후 오프닝 스킵 작업
        
    m = str(pos // 60)
    s = str(pos % 60)
    
    if len(m) == 1 : m = "0" + m
    if len(s) == 1 : s = "0" + s
        
    return "%s:%s" % (m, s)