# 25206. 너의 평점은 (실버 5)
# 알고리즘 분류 : 수학, 구현, 문자열

subjectScore = 0 # 전공과목별 합
totalScore = 0 # 학점의 총합
rankDict = {'A+' : 4.5,
            'A0' : 4.0,
            'B+' : 3.5,
            'B0' : 3.0,
            'C+' : 2.5,
            'C0' : 2.0,
            'D+' : 1.5,
            'D0' : 1.0,
            'F' : 0
            }

for _ in range(20) :
    subject, score, rank = input().split()

    if rank == 'P' :
        continue
    
    subjectScore += float(score) * rankDict[rank]
    totalScore += float(score) # 학점의 총합 갱신

print(round(subjectScore / totalScore, 6))