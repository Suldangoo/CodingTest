# 2562. �ִ� (�����3)
# �˰��� �з� : ����

n = int(input())
top = n # ù ��° ���� �׳� �Է¹��� �� top ������ ����
num = 1 # ù ��° ���� ���� ū ��ȣ��� ����

for i in range(8) : # ���� 8�� �� �Է¹���
    n = int(input())
    if top < n : # ���� n�� top���� �� ũ�ٸ�, ���ο� �ִ� ����
        # ���� ����
        top = n
        num = i + 2

print(top)
print(num)