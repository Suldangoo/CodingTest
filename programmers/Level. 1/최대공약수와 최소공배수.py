# 프로그래머스 Lv.1 최대공약수와 최소공배수

def solution(n, m): 
    # 함수를 실행한 결과를 즉시 리스트에 삽입
    return [GCD(n, m), LCM(n, m)]

# 유클리드 호제법으로 최대공약수 구하기
def GCD(x, y):
    while(y) : # y가 자연수일 때 (x % y != 0)
        x, y = y, x % y
    return x

# 최소공배수 구하기
def LCM(x, y):
    return (x * y) // GCD(x, y)