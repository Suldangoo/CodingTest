n = int(input()) # 단어의 개수

count = 0 # 그룹단어 개수

for i in range(n):
    word = input() # 단어 입력 받기
    used_alphabets = [] # 사용된 알파벳 저장할 리스트3
    flag = True # 그룹단어인지 체크하는 플래그
    
    for j in range(len(word)):
        if word[j] not in used_alphabets: # 처음 등장한 알파벳이면
            used_alphabets.append(word[j]) # 리스트에 추가
        elif word[j-1] != word[j]: # 이전 문자와 다르면서 이미 등장한 알파벳이면
            flag = False # 그룹단어가 아님
            break
    
    if flag: # 그룹단어면
        count += 1 # 그룹단어 개수 증가

print(count) # 결과 출력