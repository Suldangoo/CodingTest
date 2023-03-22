# 2920. 음계 (브론즈 2)
# 알고리즘 분류 : 구현

chord = list(map(int, input().split()))

if (chord == sorted(chord)) : # 파이썬 내장 정렬함수를 사용하여 리스트간의 비교
  print('ascending')
elif (chord == sorted(chord, reverse = True)) : # reverse 인자를 True로 하여 내림차순으로 정렬 가능
  print('descending')
else :
  print('mixed')
