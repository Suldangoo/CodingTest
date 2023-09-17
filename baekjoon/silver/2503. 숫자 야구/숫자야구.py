# 2503. 숫자 야구 (실버 3)
# 알고리즘 분류 : 구현, 브루트포스 알고리즘

def checknum(num1, num2) :
    s = 0
    b = 0

    for i in range(3) :
        if num1[i] == num2[i] : s += 1

    if num1[0] == num2[1] : b += 1
    if num1[0] == num2[2] : b += 1
    if num1[1] == num2[0] : b += 1
    if num1[1] == num2[2] : b += 1
    if num1[2] == num2[0] : b += 1
    if num1[2] == num2[1] : b += 1

    return s, b


N = int(input())
answer = []

for i in range(111, 1000) :
    tmp = str(i) # 현재 변호를 문자열로 변경

    if '0' in tmp : continue # 0이 들어갈 경우 다음 순서로 변경
    answer.append(i)

for _ in range(N) :
    num, s, b = map(int, input().split())
    num = str(num) # num을 문자열로 변경

    anslist = []

    for i in range(111, 1000) : # 111부터 999까지의 모든 수를 비교
        tmp = str(i) # 현재 변호를 문자열로 변경

        if '0' in tmp : continue # 0이 들어갈 경우 다음 순서로 변경

        s2, b2 = checknum(num, i)

        if s == s2 and b == b2 :
            anslist.append(i)

    answer = list(set(answer) & set(anslist))

print(len(answer))