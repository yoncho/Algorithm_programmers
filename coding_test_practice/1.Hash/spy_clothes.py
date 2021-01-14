#���� : https://programmers.co.kr/learn/courses/30/lessons/42578
#reduce ���� : https://www.daleseo.com/python-functools-reduce/
#lambda ���� : https://wikidocs.net/64
#Counter ���� : https://www.daleseo.com/python-collections-counter/
#
#�������� : 1. �Ѽ��� ���� 
#           (a + 1)*(b + 1)*(c + 1) - 1 = a*b*c + (a*b + b*c + c*a) + (a + b + c)
#           2. collections ���̺귯���� Counter�Լ�
#           3. functools ���̺귯���� reduce�Լ�
from collections import Counter
from functools import reduce 

# clothes�� 2�߹迭�� �����̸�,, ���� �̸� , ���� ���� �����Ͱ� �ԷµǾ��ִ�.
# clothes = [["NY cap", "headgear"]. ["Yellow_hat", "headgear"], ["sunglasses", "eyewear"]]
def solution(clothes):

    cnt = Counter([kind for name, kind in clothes])
    # [kind for name, kind in clothes] = ["headgear", "headgear", "eyewear"]
#1    Counter(..) = ["headgear" : 2, "eyewear" : 1]    
#     cnt = ["headgear" : 2, "eyewear" : 1]    �̷��� �Ǿ��ִ�.
    #         ���� Ÿ�� : �ش� Ÿ���� ���� in clothes

    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#��   reduce(lambda x, y ....)
#��   reduce�� lambda���� �Ŀ� ���Ͽ� ���� ������ش�..
#��   reduce(�����Լ�, ��ȸ ������ ������[, �ʱⰪ])   __�⺻����__
#��                                       ** [, �ʱⰪ] �� �ɼ�,, **
    # lambda ���� : ǥ����                             __�⺻����__
    # lambda�� ���� : ǥ������ �ϳ��� �Լ��� ������ش�.
    # lambda�� map(), reduce(), filter() �Լ��ȿ��� �ϳ��� �Լ��� ����ȴ�.
    # cnt�� key : value �����̴�..
    # ��, ���� Ÿ�԰� Ÿ���� �� ��� �־������� ���� ������ cnt�� ����ִ�.
    # cnt.values()�� ���� Ÿ���� ������ ����Ʈ���·� ����ȴ�.
    # cnt.values() = [2, 1]
    # 
    # reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    # reduce�� �����հ踦 ��������ش�.. 
    #  
    # lambda ���� : ����,  ��ȸ������ ������, �ʱⰪ
    # lambda x, y: x*(y+1), cnt.values(), 1
    #
    # x = 1�� �ʱⰪ���� �־��ְ�,, y���� ���� ���������� [2, 1]�� ���ҵ���
    # ����.. 
    # y = 2 �޾ƿö�,, 
    #    x = 1 (�ʱ�ȭ),   1 * ( 2 + 1 )  => x�� ����
    # y = 1 �޾ƿö�,,   
    #    x = 3         ,   3 * ( 1 + 1 )  => x�� ����
    # ���� x���� 3 * 2 = 6 �� ����ȴ�.
#2    reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1 
    # �� ����  6 - 1 �̹Ƿ� 5�� ���´�.
#3    answer = 5 ���ȴ�.
    return answer