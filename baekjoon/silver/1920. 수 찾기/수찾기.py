# 1920. 수 찾기 (실버 4)
# 알고리즘 분류 : 자료구조, 정렬, 이분 탐색

n = int(input())
a = sorted(list(map(int, input().split()))) # sorted()는 병합 정렬을 기반으로 만들어 시간복잡도 O(NlogN)를 보장
m = int(input())
b = list(map(int, input().split()))

# 파이썬 in 구문을 사용해 리스트 안 내용물을 찾으면 간단하겠지만, 이는 수가 1억개 있다면 1억번 찾아야하는 O(N)의 시간복잡도가 생김
# 즉, 배열 정렬 후 이진 탐색으로 시간복잡도를 O(logN)으로 줄일 수 있음
def binary_search (target) : 
    start = 0 # 시작 커서 정의
    end = n - 1 # 끝 커서 정의

    while start <= end : # 시작 커서가 끝 커서와 같거나 그걸 넘었다는건 원하는 데이터가 없다는 것
        middle = (start + end) // 2 # 가운데 값은 시작 커서와 끝 커서를 더하고 2를 나눈 값

        if a[middle] < target : # 찾고자 하는 데이터가 더 크다면 위로 향하게
            start = middle + 1
        elif a[middle] > target : # 찾고자 하는 데이터가 더 작다면 아래로 향하게
            end = middle - 1
        else :
            return 1
        
    return 0 # 데이터가 없으므로 0 반환

for i in b :
    print(binary_search(i))