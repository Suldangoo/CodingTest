# 프로그래머스 Lv.1 핸드폰 번호 가리기

def solution(phone_number):
    # 앞 모든 숫자를 *로 전환해 곱해 더하고, 뒤 4자리는 원본 유지
    return '*' * len(phone_number[:-4]) + phone_number[-4:]