# 프로그래머스 Lv.1 개인정보 수집 유효기간
# 2023 KAKAO BLIND RECRUITMENT

def solution(today, terms, privacies):
    answer = []

    # 오늘 날짜를 연, 월, 일로 파싱
    today_year, today_month, today_day = map(int, today.split('.'))

    # 약관 정보를 딕셔너리로 저장 (약관명을 키로, 유효기간을 값으로)
    term_dict = {}
    for term in terms:
        term_name, term_duration = term.split()
        term_dict[term_name] = int(term_duration)

    # 개인정보의 수집일자와 약관 종류를 파싱하고, 유효기간을 계산하여 오늘 날짜와 비교
    for i, privacy_info in enumerate(privacies, start=1):
        privacy_date_str, term_name = privacy_info.split()[0], privacy_info.split()[1]
        privacy_year, privacy_month, privacy_day = map(int, privacy_date_str.split('.'))

        # 유효기간 계산 (모든 달이 28일로 끝나도록 함)
        expiration_year = privacy_year + term_dict[term_name] // 12
        expiration_month = privacy_month + term_dict[term_name] % 12
        if expiration_month > 12:
            expiration_year += 1
            expiration_month -= 12
        expiration_day = min(privacy_day, 28)

        # 오늘 날짜와 유효기간을 비교하여 오늘 이후인 경우 파기 대상으로 추가
        if (today_year, today_month, today_day) >= (expiration_year, expiration_month, expiration_day):
            answer.append(i)

    return answer