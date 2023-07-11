# 11720. 숫자의 합 (브론즈 4)
# 알고리즘 분류 : 수학, 구현, 문자열

n = int(input())
num = input()
sum = 0

# 문자열을 for in으로 넣으면 한 자리씩 할당됨
for i in num :
    sum += int(i) # 그 이후에 int()를 씌워 합 계산

print(sum)