#���� : https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
#stack & queue ���� : https://devuna.tistory.com/22
#                     https://jacoblog.tistory.com/2
#
#���� ���� : stack & queue [ �ڷ� ���� ]
#            stack = �׾ƿø���, ���� ���� (LIFO : LAST IN FIRST OUT)
#            queue = ���� ���� (FIFO : FIRST IN FIRST OUT)
#
# prices ���� :  [1,2,3,2,3]
#        ��� :  [4,3,1,1,0]
def solution(prices):
    stack = []
    count = 0
    #stack �̶�� �� ����Ʈ�� ����
    #count�� ������ ������������ �Ⱓ�� �ʸ� ����� ����

    for i in range(len(prices)):
    #len(prices) = 5�̹Ƿ� i �� 0 ~ 4����
        for k in range(i + 1, len(prices)):
        #k�� i ������ �ε������� �޾ƿ;��ϹǷ�,, i+1 ~ 4����
        #prices[0]�� ���� prices[1]���� [4]���� ���ذ��鼭 �ʸ� count������ϱ⶧����
        #for�� range()������ ���� ����..

            if prices[i] > prices[k]:
            # ���� prices[0] ���� ���� ���̸� 
            # count 1�������ְ�,, for���� break�ؼ� ������.
                count += 1
                break
            else:
            # prices[0] ���� ū ���̸� count 1�������ְ� ��� for���� �۵��Ѵ�.
                count += 1
        #for���� ������ prices[i]�� ���� ���� ���ұ����� �ʰ� count�ȴ�.
        stack.append(count)
        #�׷� ���� count�� �ʸ� stack�� �׾��ش�.
        count = 0
        #�׸��� ���� i���� ���� count�� �ʱ�ȭ���ش�.
    return stack