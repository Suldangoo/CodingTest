# 4673. ���� �ѹ� (�ǹ� 5)
# �˰��� �з� : ���Ʈ����

selfNumber = []

# 0���� 10,000������ ��� �����ѹ��� selfNumber ����Ʈ�� ����
for i in range(10001) :
    i = str(i)
    num = []
    for j in i : # ���ڸ� ��� �� �ڸ��� �����Ͽ� ����Ʈ�� ����
        num.append(int(j))
    selfNumber.append(int(i) + sum(num)) # �� ���ڵ��� �հ� �� ������ ���� ����Ʈ�� ����

# selfNumber ����Ʈ�� ���ٸ� ���
for i in range(10001) :
    if not i in selfNumber :
        print(i)