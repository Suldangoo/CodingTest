# 1427. 소트인사이드 (실버 5)
# 알고리즘 분류 : 문자열, 정렬

# n = list(input())
# print(*sorted(n, reverse=True), sep='')

# 입력받은 후, 역순으로 정렬하며, 구분자가 없도록 리스트 전체를 출력
print(*sorted(input())[::-1],sep='')