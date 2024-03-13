# 프로그래머스 Lv.1 성격 유형 검사하기
# 2022 KAKAO TECH INTERNSHIP

def solution(survey, choices):    
    answer = ''
    
    # 8개의 성격 유형에 대해 하나씩 딕셔너리 형태로 저장
    score = {'R' : 0, 'C' : 0, 'J' : 0, 'A' : 0,
         'T' : 0, 'F' : 0, 'M' : 0, 'N' : 0}
    
    for i in range(len(survey)) :
        if choices[i] < 4 : # 4보다 낮을 경우
            # 앞 성격 유형에 점수를 부여
            score[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4 : # 4보다 높을 경우
            # 뒤 성격 유형에 점수를 부여
            score[survey[i][1]] += choices[i] - 4
            
    # 성격 유형 채점
    if score['R'] >= score['T'] : answer += 'R'
    else : answer += 'T'
    if score['C'] >= score['F'] : answer += 'C'
    else : answer += 'F'
    if score['J'] >= score['M'] : answer += 'J'
    else : answer += 'M'
    if score['A'] >= score['N'] : answer += 'A'
    else : answer += 'N'
            
    return answer