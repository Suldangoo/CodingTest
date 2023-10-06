# 9733. 꿀벌 (실버 5)
# 알고리즘 분류 : 구현, 자료구조, 문자여르 해시

import sys

# 꿀벌이 한 일의 딕셔너리
task = {'Re' : 0,
        'Pt' : 0,
        'Cc' : 0,
        'Ea' : 0,
        'Tb' : 0,
        'Cm' : 0,
        'Ex' : 0}

total = 0 # 총 일을 한 횟수

# 입력 케이스의 개수가 정해지지 않아있으며, EOF 처리를 위해 sys.stdin 입력
for line in sys.stdin :
    for i in list(line.split()) :
        if i in task :
            task[i] += 1 # 딕셔너리에 존재한다면 기록
        total += 1 # 일 횟수 한 번 증가

# 모든 일들을 순차대로 출력
for k, v in task.items() :
    print(k, v, end = ' ')
    print("{:.2f}".format(v / total)) # 소수 둘째자리를 위한 포맷팅

# 최종 토탈 일 출력
print("Total", total, end = ' ')
print("{:.2f}".format(total / total)) # 소수 둘째자리를 위한 포맷팅