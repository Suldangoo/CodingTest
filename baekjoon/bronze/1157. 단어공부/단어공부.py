# 1157. 단어공부 (브론즈 1)
# 알고리즘 분류 : 구현, 문자열

word = input().upper()  # 입력받은 단어를 대문자로 변환
freq = {}  # 딕셔너리 자료구조 생성
max_count = 0  # 가장 빈도수가 높은 알파벳의 빈도수를 저장할 변수

for c in word:
    if c.isalpha():  # 알파벳인 경우에만 빈도수 계산
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
        max_count = max(max_count, freq[c])  # 가장 빈도수가 높은 알파벳의 빈도수 업데이트

# 가장 빈도수가 높은 알파벳이 여러 개인 경우 ? 출력, 그렇지 않은 경우 해당 알파벳 출력
result = []
for k, v in freq.items():
    if v == max_count:
        result.append(k)

# 리스트 컴프리헨션을 사용하여 result = [k for k, v in freq.items() if v == max_count] 로 풀어쓸 수 있음

if len(result) == 1:
    print(result[0].upper())
else:
    print("?")