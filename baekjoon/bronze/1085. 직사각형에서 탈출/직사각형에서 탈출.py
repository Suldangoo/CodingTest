# 1085. ���簢������ Ż�� (�����3)
# �˰��� �з� : ����, ������

# 4���� ������ �̷���� ��ǥ���� �Է�
x, y, w, h = map(int, input().split())

distances = [x, y, w - x, h - y] # ����Ʈ�� ���� ������ 4���� ����� ���� ���̸� ����
min_distance = min(distances) # �� �� �ּڰ��� ã��

print(min_distance)
