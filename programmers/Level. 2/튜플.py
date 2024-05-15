# 프로그래머스 Lv.2 2019 카카오 개발자 겨울 인턴십 : 의상

def solution(s):
    s = s[1:-1] # 맨 앞과 뒤의 중괄호를 삭제
    
    num = '' # 숫자 문자열을 모아 숫자로 변환하는 문자열
    tuples = [] # 튜플들을 모을 리스트
    answer = [] # 정답 리스트
    
    for i in s :
        if i == '{' : # 여는 괄호라면 새로운 리스트 생성 후 숫자 수집모드로 변환
            tuples.append([])
        elif i == '}' : # 닫는 괄호라면 현재까지 모은 문자열을 숫자로 변환 후 다음 쉼표를 제거
            s = s[1:]
        elif i == ',' : # 쉼표라면 현재까지 모은 숫자 문자열을 숫자로 변환
            tuples[-1].append(int(num))
            num = ''
        else : # 남은 경우는 모두 숫자의 경우
            num += i
    tuples[-1].append(int(num)) # 반복이 끝났다면
    
    tuples.sort(key=len) # 리스트의 길이 순으로 정렬

    backupSet = set() # 이전 리스트들의 요소를 저장할 셋
    for i in tuples :
        iSet = set(i) # 현재 요소들을 셋으로 변환
        new = iSet - backupSet # 현재 요소에서 이전 요소들의 차집합을 구함
        answer.append(new.pop()) # 새로운 요소 추가
        backupSet = iSet # 백업 셋 갱신
    
    return answer