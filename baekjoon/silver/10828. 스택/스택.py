# 10828. ���� (�ǹ� 4)
# �˰��� �з� : �ڷᱸ��, ����

import sys
n = int(sys.stdin.readline())
stack = [] # ���� ������ �ϰ� �� ����Ʈ

for _ in range(n) :
    # �ݺ��� �ȿ��� �Է¹��� �ۼ��� �� �ݵ�� sys�� ����� ��
    command = list(sys.stdin.readline().split())

    if command[0] == "push" :
        stack.append(command[1])
    elif command[0] == "pop" :
        print(stack.pop()) if len(stack) != 0 else print(-1)
    elif command[0] == "size" :
        print(len(stack))
    elif command[0] == "empty" :
        print(0 if len(stack) >= 1 else 1)
    else : # top ��ɾ��� ���
        print(stack[-1]) if len(stack) != 0 else print(-1)