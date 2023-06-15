# 프로그래머스 Lv.0 머쓱이보다 키 큰 사람

# 변수 answer을 두고 array 리스트를 i에 넣는 for문을 돌린다
def solution(array, height):
    answer = 0 # 사람 수를 0으로 초기화
    for i in array :
        if height < i : # 만약 리스트의 내용물이 머쓱이의 키보다 크다면
            answer += 1 # 사람 수를 1명 추가시킨다
    return answer