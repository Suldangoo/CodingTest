word = input().upper()  # �Է¹��� �ܾ �빮�ڷ� ��ȯ
freq = {}  # ��ųʸ� �ڷᱸ�� ����
max_count = 0  # ���� �󵵼��� ���� ���ĺ��� �󵵼��� ������ ���� �ʱ�ȭ

for c in word:
    if c.isalpha():  # ���ĺ��� ��쿡�� �󵵼� ���
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
        max_count = max(max_count, freq[c])  # ���� �󵵼��� ���� ���ĺ��� �󵵼� ������Ʈ

# ���� �󵵼��� ���� ���ĺ��� ���� ���� ��� ? ���, �׷��� ���� ��� �ش� ���ĺ� ���
result = [k for k, v in freq.items() if v == max_count]
if len(result) == 1:
    print(result[0].upper())
else:
    print("?")