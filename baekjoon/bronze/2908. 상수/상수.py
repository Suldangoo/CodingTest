# 2908. ��� (����� 2)
# �˰��� �з� : ����, ����

a, b = input().split()

# ������ ���� ��
a_reverse = int(a[::-1])
b_reverse = int(b[::-1])

# ū �� ���
print(max(a_reverse, b_reverse))