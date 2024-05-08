# 프로그래머스 Lv.2 행렬의 곱셈

def solution(arr1, arr2):
    # arr1의 행 수와 arr2의 열 수로 이루어진 새로운 행렬을 생성
    n = len(arr1)
    m = len(arr2[0])
    answer = [[0 for j in range(m)] for i in range(n)]
    
    # arr2의 각 열만으로 이루어진 새로운 행렬 생성    
    columns = [[row[i] for row in arr2] for i in range(len(arr2[0]))]
    
    # 두 행렬 곱하기
    for i in range(n) :
        for j in range(m) :
            answer[i][j] = sum([x * y for x, y in zip(arr1[i], columns[j])])
    
    return answer