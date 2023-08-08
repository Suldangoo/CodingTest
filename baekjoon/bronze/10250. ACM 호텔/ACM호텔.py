# 10250. ACM 호텔 (브론즈 3)
# 알고리즘 분류 : 구현, 사칙연산

T = int(input())

for _ in range(T) :
    H, W, N = map(int, input().split())
    back = 1 # 뒤 호수로 쓰일 숫자

    while (N > H) :
        N -= H # 층만큼의 수를 빼 뒤 호수가 몇 호일지 결정
        back += 1

    print(N * 100 + back) # 남은 수에 100을 곱해 앞 호수가 몇 호일지 결정