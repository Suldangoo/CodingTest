# 3052. ������ (����� 2)
# �˰��� �з� : ����, ��Ģ����

# �ߺ��� �����ϱ� ���� �� set ����
nums = set()

for _ in range(10) : 
    num = int(input()) % 42 # �Է¹��� ���� 42�� ���� �������� ����
    nums.add(num) # set�� add

print(len(nums)) # set�� ���� ���