# 프로그래머스 Lv.1 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]] # arr의 첫 번째 원소 추가
    
    # arr의 첫 번째 원소를 제외한 나머지 리스트에 대해 반복
    for i in arr[1:] :
        # answer 리스트의 마지막 요소와 현재 요소가 다르다면 삽입
        if answer[-1] != i :
            answer.append(i)
    
    return answer