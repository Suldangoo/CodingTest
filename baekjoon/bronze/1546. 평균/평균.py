# 1546. ��� (�����1)
# �˰��� �з� : ����, ��Ģ����

n = int(input())
score = list(map(int, input().split())) # ����Ʈ�� ���� �Է¹ޱ�
score = sorted(score) # �迭�� ����

# ù ��° ���� ���������� ���ϴ� ���·� ��ȯ
# ������ ĭ�� ���� ū �����̹Ƿ� ������ ������ ������ �� �ʿ�� ����
for i in range(n) :
    score[i] = score[i] / score[-1] * 100

print(sum(score) / len(score)) # ��� ���