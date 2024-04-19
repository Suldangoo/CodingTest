# 프로그래머스 Lv.1 행렬의 덧셈

def solution(arr1, arr2):
    row = len(arr1) # 행의 길이 측정
    column = len(arr1[0]) # 열의 길이 측정
    
    for r in range(row) :
        for c in range(column) :
            arr1[r][c] += arr2[r][c]
    
    return arr1