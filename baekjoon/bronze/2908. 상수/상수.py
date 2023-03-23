# 2908. 상수 (브론즈 2)
# 알고리즘 분류 : 수학, 구현

a, b = input().split()

# 뒤집은 수를 비교
a_reverse = int(a[::-1])
b_reverse = int(b[::-1])

# 큰 수 출력
print(max(a_reverse, b_reverse))