# 그리디(Greedy, 욕심쟁이) 알고리즘 문제 : 큰 수의 법칙
# 불규칙적인 정수들의 배열이 주어졌을 때, 해당 정수들을 사용해 더하여 가장 큰 수를 만들어라
# 첫 줄에 배열의 길이 / 몇 번 더할 수 있는지 / 한 숫자를 연속으로 사용할 수 있는 횟수 제한이 주어진다
# 두 번째 줄에 배열의 내용이 주어진다

n, m, k = map(int, input().split()) # n, m, k를 입력받음
data = list(map(int, input().split())) # n개만큼 입력을 받은 후 리스트로 변경
data = sorted(data) # 정렬, 오름차순이므로 가장 뒤에와 거기서 앞 숫자가 가장 큰 두 숫자

one = data[-1] # 가장 큰 숫자 인덱싱
two = data[-2] # 두 번째로 큰 숫자 인덱싱
total = 0 # 합 계
flag = 0 # 연속 k번을 감지하기 위한 플래그 변수

for _ in range(m) : # m번만큼 반복
    if flag >= k : # 플래그가 k와 같다면
        total += two # 2번째로 큰 수를 더함
        flag = 0 # 플래그 정상화
    else :
        total += one
        flag += 1 # 플래그를 1씩 올림

print(total)