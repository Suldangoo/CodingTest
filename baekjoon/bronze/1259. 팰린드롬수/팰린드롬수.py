# 1259. �Ӹ���Ҽ� (����� 1)
# �˰��� �з� : ����, ���ڿ�

def is_palindrome(n):
    # �Է¹��� ���� ���ڿ��� ��ȯ�ϰ�, �������� ������ ���ڿ��� ���Ѵ�.
    return str(n) == str(n)[::-1]

while True:
    n = int(input())
    if n == 0:
        break
    if is_palindrome(n):
        print('yes')
    else:
        print('no')