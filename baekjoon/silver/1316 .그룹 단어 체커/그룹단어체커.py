# 1316. �׷� �ܾ� üĿ (�ǹ�5)
# �˰��� �з� : ����, ���ڿ�

n = int(input()) # �ܾ��� ����

count = 0 # �׷�ܾ� ����

for i in range(n):
    word = input() # üũ�� �ܾ�
    used_alphabets = [] # ���� ���ĺ��� ������ ����Ʈ
    flag = True # �׷�ܾ����� üũ�ϴ� �÷���, �켱 �׷� �ܾ����� �����ϰ� ����
    
    # �ܾ��� ���̸�ŭ �ݺ����� ������
    for j in range(len(word)):
        if word[j] not in used_alphabets: # ó�� ������ ���ĺ��̸�
            used_alphabets.append(word[j]) # ����Ʈ�� �߰�
        elif word[j-1] != word[j]: # ���� ���ڿ� �ٸ��鼭 �̹� ������ ���ĺ��̸�
            flag = False # �׷�ܾ �ƴ�
            break
    
    if flag: # �׷�ܾ��
        count += 1 # �׷�ܾ� ���� ����

print(count) # ��� ���