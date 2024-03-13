# 거듭제곱해 만들 수 있는 숫자 크기 순으로 나열한 수열을 거듭제곱 수열이라고 한다.
# 예를 들어, 1, 4, 8, 9, 16, 25, 27, 32, 36...
# 자연수 n이 매개변수로 주어질 때, 거듭제곱 수열에서 n번째 숫자를 return하도록 함수를 작성하시오.
# 제한사항 : n은 1 이상, 1,000,000 이하인 자연수이다.

# 입력 1 -> 출력 1 (1의 제곱)
# 입력 4 -> 출력 9 (3의 제곱)
# 입력 7 -> 출력 27 (3의 세제곱)

def solution(n) :
    powers = set()
    
    for base in range(1, 1001):
        power = 2
        while True:
            result = base ** power
            if result > 1000000**2: # 1,000,000의 제곱보다 큰 수를 벗어나면 break
                break
            powers.add(result)
            power += 1
    
    sorted_powers = sorted(list(powers))
    return sorted_powers[n-1]