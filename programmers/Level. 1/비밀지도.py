# 프로그래머스 Lv.1 [1차] 비밀지도
# 2018 KAKAO BLIND RECRUITMENT

def binaryChange(n, arr) :
    tmp = [format(i, 'b') for i in arr] # 2진수로 바꾼 리스트 생성
    result = []
    
    for i in tmp :
        result.append(str(i).rjust(n, '0')) # 길이에 맞춰서 빈 공간에 0을 채운 문자열로 변경
    
    return result

def solution(n, arr1, arr2):
    answer = []
    map1 = binaryChange(n, arr1)
    map2 = binaryChange(n, arr2)
    
    for i in range(n) :
        string = '' # #으로 채워질 문자열
        for j in range(n) :
            if map1[i][j] == '1' or map2[i][j] == '1' : # or로 풀이
                string += '#'
            else :
                string += ' '
        answer.append(string)
    
    return answer