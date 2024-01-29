def solution(keymap, targets):
    answer = [] # 정답 리스트
    
    # 타겟의 앞 문자열부터 확인
    for i in targets :
        dept = 0 # 클릭의 최소 횟수 초기화
        
        # 가져온 문자열의 앞 문자부터 확인
        for j in i :
            m = 101 # 최소한의 클릭 횟수
            
            # 키맵의 문자열들을 차례로 가져옴
            for k in keymap :
                if j in k : # 만약 문자열에 원하는 문자가 존재한다면
                    m = min(m, k.index(j) + 1) # 최소 클릭 횟수를 불러옴
            # 클릭 횟수가 100보다 작다면, 클릭이 되었다고 판단하고 더하기
            if m <= 100 :
                dept += m
            # 문자들 중 하나라도 클릭이 불가능하다면, dept를 초기화하고 반복문 종료
            else :
                dept = 0
                break
        
        # 클릭 횟수가 하나도 없다면 -1로 변환
        if dept == 0 :
            dept = -1
            
        # 정답 배열에 답 추가
        answer.append(dept)
    
    return answer