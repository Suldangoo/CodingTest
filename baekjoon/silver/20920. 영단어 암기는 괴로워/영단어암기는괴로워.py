# 20920. 영단어 암기는 괴로워 (실버 3)
# 알고리즘 분류 : 자료 구조, 문자열, 정렬, 해시

import sys
input = sys.stdin.readline

note = dict() # 단어장으로 만들 딕셔너리 생성

N, M = map(int, input().split()) # 개수와 암기 글자 입력

for _ in range(N) :
    # 단어를 입력받을 때, 공백을 제거
    word = input().rstrip()
    if len(word) >= M : # 반드시 M자 이상의 단어만을 암기
        if word in note : # 만약 해당 단어가 키로서 딕셔너리에 존재 시 1 추가
            note[word] += 1
        else : # 아니라면 해당 단어를 키로 단어장에 추가
            note[word] = 1

# 우선순위의 역순으로 정렬
# 알파벳 사전 순 정렬 - 단어의 길이 내림차순 정렬 - 자주 나오는 단어일 수록 앞 정렬

note = dict(sorted(note.items())) # 키 알파벳 순 정렬
note = dict(sorted(note.items(), key=lambda x: len(x[0]), reverse=True)) # 단어 길이 내림차순 정렬
note = dict(sorted(note.items(), key=lambda x: x[1], reverse=True)) # 자주 나오는 단어순 정렬

for k in note.keys() :
    print(k) # 키 나열