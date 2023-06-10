# 1065. 한수 (실버 4)
# 알고리즘 분류 : 브루트포스

n = int(input())

if n < 100 : # n이 100보다 작다면 반드시 해당 숫자가 한수의 개수
    print(n)
elif n == 1000 : # n이 1000이라면 반드시 한수의 개수는 144 고정
    print(144)
else : # 사전 공격이 끝났으므로 111보다 큰 3자리 정수의 브루트포스 알고리즘 작동
    ans = 99 # 우선 99개임을 기본으로 지정
    for i in range(111, n + 1) : # 111부터 사용자가 입력한 정수까지 반복
        num = []
        for j in map(int, str(i)) : # 해당 숫자를 split으로 갈라 리스트에 추가
            num.append(j)

        if num[0] - num[1] == num[1] - num[2] : # 1번 ~ 3번의 자리가 등차수열이면, 한수
            ans += 1
    print(ans)