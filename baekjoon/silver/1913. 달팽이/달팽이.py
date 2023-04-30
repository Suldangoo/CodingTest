# 1913. 달팽이 (실버 3)
# 알고리즘 분류 : 구현

n = int(input())
find = int(input())

# 숫자를 채워넣을 빈 테이블 생성
table = [[0 for _ in range(n)] for _ in range(n)]
x = y = n // 2 # x좌표와 y좌표 선정
num = 0 # 1부터 n^2 까지 상승할 숫자
mode = 0 # 상하좌우중 어디로 이동할지 결정할 변수
jump = 1 # 몇 칸 이동할지 결정할 변수

while True :
    # jump번 반복한다
    for _ in range(jump) :
        num += 1 # num을 1 상승한다
        table[x][y] = num # 현재 좌표에 num을 저장한다
        # 만약 찾고있던 숫자라면 해당 좌표를 저장한다
        if num == find :
            findx = x
            findy = y
        # mode 변수에 따라 x 혹은 y를 이동시킨다
        if mode == 0 :
            x -= 1
        elif mode == 1 :
            y += 1
        elif mode == 2 :
            x += 1
        elif mode == 3 :
            y -= 1
        # 마지막 숫자에 도달했다면 break한다
        if num >= n ** 2 :
            break
    
    # jump번 반복했다면 모드를 변경한다
    mode = (mode + 1) % 4

    # 모드가 두 번 바뀔 때마다 jump 변수를 증가시킨다
    if mode % 2 == 0 :
        jump += 1

    # 마지막 숫자에 도달했다면 break한다
    if num >= n ** 2 :
            break

for i in table :
    for j in i :
        print(j, end = ' ')
    print()

print(findx + 1, findy + 1)