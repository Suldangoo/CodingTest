# 1085. ���簢������ Ż�� (�����3)
# �˰��� �з� : ����, ������

# �Ѽ��� ��ġ ��ǥ�� ���簢���� ũ�Ⱚ �Է�
x, y, w, h = map(int, input().split())

distances = [x, y, w - x, h - y] # �����¿� �������� Ż���ϴ� ��� �Ÿ��� ����
min_distance = min(distances) # ���� �ּڰ��� ����

print(min_distance)
