# 8958. OX���� (�����2)
# �˰��� �з� : ����, ���ڿ�

n = int(input())

for _ in range(n) :
    score = 0 # ����
    plus = 0 # 1�� �������� ���ӹ��� ����
    ox = input()
    for i in ox : # ���ڿ��� for������ ������ �� ���ھ� ��
        if i == 'O' :
            plus += 1 # ���ӹ��� ������ 1���� ���ϰ�
            score += plus # ������ ����
        else :
            plus = 0 # X�� ���Դٸ� plus ������ �ʱ�ȭ
    print(score)