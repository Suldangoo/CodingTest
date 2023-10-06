# 1620. 나는야 포켓몬 마스터 이다솜 (실버 4)
# 알고리즘 분류 : 자료구조, 해시

# 입력이 많으므로 sys 사용
import sys
input = sys.stdin.readline

# 파이썬의 경우 Hash 구조를 Dictionary를 통해 제공

N, M = map(int, input().split())
pokemon = {} # 포켓몬 도감
problem = [] # 문제들
answer = {} # 정답들

# 도감 딕셔너리에 1번부터 포켓몬의 이름을 삽입
for i in range(1, N + 1) :
    pokemon[i] = input().rstrip()

# 문제를 리스트에 입력받는데, 숫자일 경우 숫자로 변환하여 삽입
for i in range(M) :
    tmp = input().rstrip()
    if tmp.isdigit() :
        tmp = int(tmp)

    problem.append(tmp)

# 도감을 for문으로 싹 훑어봄
for k, v in pokemon.items() :

    # 번호가 문제 안에 존재하는 경우
    if k in problem :
        # 해당 배열의 인덱스값을 키로 이름을 저장
        answer[problem.index(k)] = v
    
    # 포켓몬 이름이 문제 안에 존재하는 경우
    if v in problem :
        # 해당 배열의 인덱스값을 키로 번호를 저장
        answer[problem.index(v)] = k

# 키를 기준으로 딕셔너리 정렬
answer = sorted(answer.items())

for i in answer :
    # 튜플 형태로 저장되어있기 때문에, 1번지를 모두 출력
    print(i[1])