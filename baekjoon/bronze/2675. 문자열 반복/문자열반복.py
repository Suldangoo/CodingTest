# 2675. ������ �� (����� 2)
# �˰��� �з� : ����, ���ڿ�

for i in range(int(input())) :
    r, s = input().split()
    r = int(r)

    for j in range(len(s)) :
        print(r * s[j], end = "") # ���̽��� ���ڿ� * ���� ����� ���

    print() # �ٳѱ��� ���־�� ������ �Ǿ� ���� ����¿� ���� �ùٸ��� ��µ�