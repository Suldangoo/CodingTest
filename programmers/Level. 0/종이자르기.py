# 프로그래머스 Lv.0 종이 자르기

# 한 변에 나눠질 종이 M x N 이 주어졌을 때, 최소 가위질 수는
# M 과 N을 곱한 결과에서 -1이다.
def solution(M, N):
    answer = (M * N) - 1
    return answer