# 2503. 숫자 야구 (실버 3)
# 알고리즘 분류 : 구현, 브루트포스 알고리즘

def checknum(num1, num2) :
    s = 0
    b = 0

    # 스트라이크 체크
    for i in range(3) :
        if num1[i] == num2[i] : s += 1

    # 볼 체크
    if num1[0] == num2[1] : b += 1
    if num1[0] == num2[2] : b += 1
    if num1[1] == num2[0] : b += 1
    if num1[1] == num2[2] : b += 1
    if num1[2] == num2[0] : b += 1
    if num1[2] == num2[1] : b += 1

    return s, b


N = int(input())
answer = []

for i in range(123, 988) :
    tmp = str(i) # 현재 변호를 문자열로 변경

    if '0' in tmp : continue # 0이 들어갈 경우 다음 순서로 변경
    if len(tmp) > len(set(tmp)) : continue # 중복 문자열이 있을 경우 다음 순서로 변경

    # 모든 경우를 리스트에 담아둠
    answer.append(tmp)

for _ in range(N) :
    num, s, b = map(int, input().split())
    num = str(num) # num을 문자열로 변경

    anslist = []

    for i in range(123, 988) : # 123부터 987까지의 모든 수를 비교
        tmp = str(i) # 현재 변호를 문자열로 변경

        if '0' in tmp : continue # 0이 들어갈 경우 다음 순서로 변경
        if len(tmp) > len(set(tmp)) : continue # 중복 문자열이 있을 경우 다음 순서로 변경

        # 스트라이크와 볼 체크
        s2, b2 = checknum(num, tmp)

        if s == s2 and b == b2 : # 적합할 경우 리스트에 추가
            anslist.append(tmp)

    # 리스트의 교집합을 구함
    answer = list(set(answer) & set(anslist))

print(len(answer)) # 리스트 길이 출력