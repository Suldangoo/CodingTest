# 1541. 잃어버린 괄호 (실버 2)
# 알고리즘 분류 : 수학, 그리디 알고리즘, 문자열, 파싱

expression = input().split('-') # '-'를 기준으로 잘라낸 문자열들을 수집
minusList = [] # 모두 빼야하는 수들만을 담아낸 리스트

for i in expression :
    if '+' in i : # 만약 '+'가 있는 수식이라면
        minusList.append(sum(map(int, i.split('+')))) # 모두 더한 후 int 형태로 저장
    else : # 만약 수 하나만 있다면
        minusList.append(int(i)) # int 형태로 저장

print(minusList[0] - sum(minusList[1:])) # 첫 번째 수 - 나머지 모든 수들의 합 출력