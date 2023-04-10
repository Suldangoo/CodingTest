# 14501. ��� (�ǹ� 3)
# �˰��� �з� : ���̳��� ���α׷���, ���Ʈ ����, ����

import sys

n = int(sys.stdin.readline()) # ��� �� ��
t = [] # �� ��㿡 �ҿ�Ǵ� �ϼ�
p = [] # �� ��㿡 ���� ����
dp = [0] * (n + 1) # �� ��¥�� �ִ� ����

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    t.append(x)
    p.append(y)

# �������� dp ���
for i in range(n - 1, -1, -1):
    if i + t[i] > n: # ��� �Ⱓ�� ������� �ʰ��ϴ� ���
        dp[i] = dp[i + 1] # ���� �ִ� �������� ��ü
    else:
        dp[i] = max(dp[i + 1], dp[i + t[i]] + p[i]) # ���� �ִ� ���Ͱ� ���ο� ���� + �ش� ��� �� ���� ���� �� ū �� ����

print(dp[0]) # ���� �ִ� ���� ���