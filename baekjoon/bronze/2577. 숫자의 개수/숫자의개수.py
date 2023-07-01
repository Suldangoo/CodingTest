# 2577. 숫자의 개수 (브론즈 2)
# 알고리즘 분류 : 수학, 구현, 사칙연산

a = int(input())
b = int(input())
c = int(input())

num = list(str(a * b * c)) # 문자열로 바꾼 뒤 리스트로 만들어 한 글자씩 split()

for i in range(10) :
    print(num.count(str(i))) # 문자인 i가 해당 리스트에 몇 개 있는지 count()