# ���α׷��ӽ� Lv.0 �Ӿ��̺��� Ű ū ���

# ���� answer�� �ΰ� array ����Ʈ�� i�� �ִ� for���� ������
def solution(array, height):
    answer = 0 # ��� ���� 0���� �ʱ�ȭ
    for i in array :
        if height < i : # ���� ����Ʈ�� ���빰�� �Ӿ����� Ű���� ũ�ٸ�
            answer += 1 # ��� ���� 1�� �߰���Ų��
    return answer