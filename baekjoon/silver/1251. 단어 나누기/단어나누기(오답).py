# 1251. 단어 나누기 (실버 5)
# 알고리즘 분류 : 구현, 문자열, 브루트포스 알고리즘, 정렬

import sys
input = sys.stdin.readline

ward = input() # 단어를 입력받음

point1 = 0 # 첫 번째로 슬라이싱할 문자의 번지수

for i in range(len(ward) - 2) :
    if ward[point1] > ward[i] : # 만약 현재 번지수의 문자가 저장해뒀던 문자보다 작다면
        point1 = i

point2 = point1 + 1 # 두 번째로 슬라이싱할 문자의 번지수

for i in range(point1 + 1, len(ward) - 1) :
    if ward[point2] > ward[i] : # 만약 현재 번지수의 문자가 저장해뒀던 문자보다 작다면
        point2 = i

print(''.join(
    list(reversed(ward[:point1 + 1])) + 
    list(reversed(ward[point1 + 1:point2 + 1])) + 
    list(reversed(ward[point2 + 1:-1]))))

# aaaab같은 문자열을 뒤집었을 때 답이 aaaab가 나와야 하나, aabaa가 나오는 반례가 존재