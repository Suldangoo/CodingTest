def solution(s, skip, index):
    answer = ''
    
    # 문자열 하나씩 처리
    for i in s :
        loop = index # loop 변수 초기화
        
        # loop가 1 이상일 경우 반복
        while loop :
            # 현재 문자열의 아스키코드가 122(z)라면
            if ord(i) >= 122 :
                i = 'a' # a로 변경
            else :
                i = chr(ord(i) + 1) # 다음 알파벳으로 변환
            
            # 현재 알파벳이 skip 리스트에 존재하지 않는다면
            if i not in skip :
                loop -= 1 # loop 변수 감소
                
        answer += i # 문자열 추가
    
    return answer