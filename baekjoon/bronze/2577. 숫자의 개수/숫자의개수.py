# 2577. ������ ���� (����� 2)
# �˰��� �з� : ����, ����, ��Ģ����

a = int(input())
b = int(input())
c = int(input())

num = list(str(a * b * c)) # ���ڿ��� �ٲ� �� ����Ʈ�� ����� �� ���ھ� split()

for i in range(10) :
    print(num.count(str(i))) # ������ i�� �ش� ����Ʈ�� �� �� �ִ��� count()