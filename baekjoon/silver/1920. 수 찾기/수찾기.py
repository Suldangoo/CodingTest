# 1920. �� ã�� (�ǹ� 4)
# �˰��� �з� : �ڷᱸ��, ����, �̺� Ž��

n = int(input())
a = sorted(list(map(int, input().split()))) # sorted()�� ���� ������ ������� ����� �ð����⵵ O(NlogN)�� ����
m = int(input())
b = list(map(int, input().split()))

# ���̽� in ������ ����� ����Ʈ �� ���빰�� ã���� �����ϰ�����, �̴� ���� 1�ﰳ �ִٸ� 1��� ã�ƾ��ϴ� O(N)�� �ð����⵵�� ����
# ��, �迭 ���� �� ���� Ž������ �ð����⵵�� O(logN)���� ���� �� ����
def binary_search (target) : 
    start = 0 # ���� Ŀ�� ����
    end = n - 1 # �� Ŀ�� ����

    while start <= end : # ���� Ŀ���� �� Ŀ���� ���ų� �װ� �Ѿ��ٴ°� ���ϴ� �����Ͱ� ���ٴ� ��
        middle = (start + end) // 2 # ��� ���� ���� Ŀ���� �� Ŀ���� ���ϰ� 2�� ���� ��

        if a[middle] < target : # ã���� �ϴ� �����Ͱ� �� ũ�ٸ� ���� ���ϰ�
            start = middle + 1
        elif a[middle] > target : # ã���� �ϴ� �����Ͱ� �� �۴ٸ� �Ʒ��� ���ϰ�
            end = middle - 1
        else :
            return 1
        
    return 0 # �����Ͱ� �����Ƿ� 0 ��ȯ

for i in b :
    print(binary_search(i))