# 프로그래머스 Lv.1 로또의 최고 순위와 최저 순위
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)

def solution(lottos, win_nums):
    answer = []
    barely = 0 # 모르는 로또 번호의 개수
    rank = 7 # 현재 로또의 순위 (7부터 시작)
    
    for i in lottos :
        if i == 0 : # 불러온 수가 0이라면 모르는 로또 번호
            barely += 1
        elif i in win_nums :
            rank -= 1 # 해당 수가 당첨번호에 있다면 랭킹 1 감소
            
    # 순위를 책정할 때, 7위부터 시작했으므로 반드시 6과 대조해야 함
    answer.append(min(6, rank - barely)) # 최고 순위는 현재 로또 순위에서 모르는 번호를 뺀 만큼
    answer.append(min(6, rank)) # 최저 순위는 현재 로또 순위
    
    return answer