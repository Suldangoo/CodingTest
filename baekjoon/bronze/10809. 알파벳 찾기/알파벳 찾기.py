# 10809. 알파벳 찾기 (브론즈 2)
# 알고리즘 분류 : 구현, 문자열

word = input() # 단어를 입력받음
positions = [-1] * 26 # 알파벳의 위치를 저장할 리스트를 -1로 초기화

for i in range(len(word)): # 단어의 길이만큼 반복
    idx = ord(word[i]) - 97 # 알파벳의 위치를 인덱스로 변환
    if positions[idx] == -1: # 만약 해당 알파벳이 처음 등장한 경우
        positions[idx] = i # 알파벳의 위치를 저장

for pos in positions: # 알파벳의 위치를 출력
    print(pos, end=' ')