# 10809. ���ĺ� ã�� (����� 2)
# �˰��� �з� : ����, ���ڿ�

word = input() # �ܾ �Է¹���
positions = [-1] * 26 # ���ĺ��� ��ġ�� ������ ����Ʈ�� -1�� �ʱ�ȭ

for i in range(len(word)): # �ܾ��� ���̸�ŭ �ݺ�
    idx = ord(word[i]) - 97 # ���ĺ��� ��ġ�� �ε����� ��ȯ
    if positions[idx] == -1: # ���� �ش� ���ĺ��� ó�� ������ ���
        positions[idx] = i # ���ĺ��� ��ġ�� ����

for pos in positions: # ���ĺ��� ��ġ�� ���
    print(pos, end=' ')