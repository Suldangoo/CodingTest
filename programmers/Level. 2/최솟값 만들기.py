# 프로그래머스 Lv.2 최솟값 만들기

def solution(A,B):
    # 곱셈은 큰 수끼리 곱해질 수록 더 큰 숫자가 나오므로, 최대한 한쪽 수는 작게, 한쪽 수는 크게 두어 곱셈할 것
    answer = 0

    A.sort() # 오름차순 정렬
    B.sort(reverse=True) # 내림차순 정렬
    
    # 각 원소를 곱하여 합을 누적
    for i in range(len(A)) :
        answer += A[i] * B[i]

    return answer