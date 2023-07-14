# 1316. 그룹 단어 체커 (실버5)
# 알고리즘 분류 : 구현, 문자열

n = int(input()) # 단어의 개수

count = 0 # 그룹단어 개수

for i in range(n):
    word = input() # 체크할 단어
    used_alphabets = [] # 사용된 알파벳을 저장할 리스트
    flag = True # 그룹단어인지 체크하는 플래그, 우선 그룹 단어임을 상정하고 시작
    
    # 단어의 길이만큼 반복문을 돌릴것
    for j in range(len(word)):
        if word[j] not in used_alphabets: # 처음 등장한 알파벳이면
            used_alphabets.append(word[j]) # 리스트에 추가
        elif word[j-1] != word[j]: # 이전 문자와 다르면서 이미 등장한 알파벳이면
            flag = False # 그룹단어가 아님
            break
    
    if flag: # 그룹단어면
        count += 1 # 그룹단어 개수 증가

print(count) # 결과 출력