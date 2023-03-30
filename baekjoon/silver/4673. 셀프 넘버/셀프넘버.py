# 4673. 셀프 넘버 (실버 5)
# 알고리즘 분류 : 브루트포스

selfNumber = []

# 0부터 10,000까지의 모든 셀프넘버를 selfNumber 리스트에 저장
for i in range(10001) :
    i = str(i)
    num = []
    for j in i : # 숫자를 모두 한 자리씩 분할하여 리스트에 저장
        num.append(int(j))
    selfNumber.append(int(i) + sum(num)) # 그 숫자들의 합과 본 숫자의 합을 리스트에 저장

# selfNumber 리스트에 없다면 출력
for i in range(10001) :
    if not i in selfNumber :
        print(i)