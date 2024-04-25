# 2941. 크로아티아 알파벳 (실버 5)
# 알고리즘 분류 : 문자열, 구현

words = input()

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = 0

while len(words) :
    if len(words) == 1 : # 한 글자만 남았다면
        words = ''
    elif words[:2] in alphabet : # 앞 두 글자가 크로아티아 알파벳이라면
        words = words[2:]
    elif words[:3] in alphabet : # 앞 세 글자가 크로아티아 알파벳이라면
        words = words[3:]
    else : # 모두 아니라면
        words = words[1:]

    answer += 1

print(answer)