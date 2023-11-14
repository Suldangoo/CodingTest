# 1251. 단어 나누기 (실버 5)
# 알고리즘 분류 : 구현, 문자열, 브루트포스 알고리즘, 정렬

import sys
input = sys.stdin.readline

ward = input().strip() # 단어를 입력받음

wards = [] # 모든 거꾸로된 경우의 단어들을 저장할 리스트

# 슬라이싱할 리스트의 끝번호를 기준으로 변수를 두 개 설정
for i in range(1, len(ward) - 1) : # 1 ~ 길이 - 2까지
    for j in range(i + 1, len(ward)) : # i + 1 ~ 길이 - 1까지
        # 모든 조합을 모음
        wards.append(''.join(list(reversed(ward[:i])) +
                     list(reversed(ward[i:j])) +
                     list(reversed(ward[j:]))))
        
# 정렬 후 가장 앞에있는 단어조합 출력
print(sorted(wards)[0])