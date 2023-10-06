# 1620. 나는야 포켓몬 마스터 이다솜 (실버 4)
# 알고리즘 분류 : 자료구조, 해시

# 입력이 많으므로 sys 사용
import sys
input = sys.stdin.readline

# 파이썬의 경우 Hash 구조를 Dictionary를 통해 제공

N, M = map(int, input().split())
pokemon = {} # 포켓몬 도감

for i in range(1, N + 1) :
    tmp = input().rstrip()
    # 키와 값을 모두 딕셔너리에 각각 넣어줌
    pokemon[i] = tmp
    pokemon[tmp] = i

for _ in range(M) :
    problem = input().rstrip()

    # 만약 입력값이 숫자일 경우엔 숫자로 변환하여 출력
    if problem.isdigit() :
        print(pokemon[int(problem)])
    else :
        print(pokemon[problem])