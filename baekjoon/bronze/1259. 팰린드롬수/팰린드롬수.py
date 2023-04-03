# 1259. 팰린드롬수 (브론즈 1)
# 알고리즘 분류 : 구현, 문자열

def is_palindrome(n):
    # 입력받은 수를 문자열로 변환하고, 역순으로 뒤집은 문자열과 비교한다.
    return str(n) == str(n)[::-1]

while True:
    n = int(input())
    if n == 0:
        break
    if is_palindrome(n):
        print('yes')
    else:
        print('no')