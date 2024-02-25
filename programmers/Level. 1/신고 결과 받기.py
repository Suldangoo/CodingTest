# 프로그래머스 Lv.1 신고 결과 받기
# 2022 KAKAO BLIND RECRUITMENT

def solution(id_list, report, k):
    data = dict() # 키가 유저 ID고, 값이 유저가 신고한 ID들로 이루어진 리스트인 딕셔너리
    report_data = dict() # 키가 유저 ID고, 값이 해당 유저가 신고당한 수인 딕셔너리
    answer = [] # 정답을 담을 리스트
    
    # ID별로 빈 리스트를 생성, 딕셔너리 초기화
    for id in id_list :
        data[id] = []
        report_data[id] = 0
    
    # 신고데이터 처리
    for item in report:
        i, j = item.split()
        # 신고 데이터에 존재하지 않다면 추가하고 신고횟수 증가
        if j not in data[i]:
            data[i].append(j)
            report_data[j] += 1
        
    # 최종 처리 결과 메일 횟수 처리
    for v in data.values() :
        temp = 0 # 처리 결과 메일 전송 횟수
        for i in v :
            if report_data[i] >= k : # 신고한 ID들을 살펴보고, 신고 횟수를 넘겼다면
                temp += 1 # 처리 결과 메일 1회 전송
        answer.append(temp) # 최종 값을 answer에 삽입

    return answer