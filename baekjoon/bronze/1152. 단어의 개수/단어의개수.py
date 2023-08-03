# 1152. 단어의 개수 (브론즈 2)
# 알고리즘 분류 : 구현, 문자열

string = input().strip() # 문자열 입력받기 (양쪽 공백 제거)

# 문자열을 공백을 기준으로 분리하여 리스트에 저장
words = string.split()

# 분리된 단어의 개수를 출력
print(len(words))