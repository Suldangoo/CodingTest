# 프로그래머스 Lv.1 나머지가 1이 되는 수 찾기

def solution(n):
    
    for i in range(2, n) : # 그 수가 어떻든 반드시 n-1은 1로 나누어 떨어짐
        if n % i == 1 : # 나머지가 1이 되면 출력
            return i