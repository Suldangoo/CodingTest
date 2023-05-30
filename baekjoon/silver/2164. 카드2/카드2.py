# 2164. 카드2 (실버 4)
# 알고리즘 분류 : 자료구조, 큐

# collections.deque 데크 라이브러리 사용
from collections import deque

n = int(input())
card = deque() # 새로운 큐 생성

# 사용자가 입력한 숫자만큼의 카드 삽입
for i in range(n) :
    card.append(i + 1)

# 카드가 한 장 남을 때까지 반복
while(len(card) > 1) :
    card.popleft() # 가장 왼쪽의 카드를 제거
    card.append(card.popleft()) # 가장 왼쪽의 카드를 제거하면서 새로이 추가

print(card[0]) # 마지막 남은 카드 하나를 출력