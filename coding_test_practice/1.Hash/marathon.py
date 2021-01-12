#1�� �ڵ�
#���� : participant���� �����濡 ������ �������� �̸��� ��� �迭 , 
#       completion���� �������� ������ �������� �̸��� ����ִ�. 
#       (*��, �������� �� �Ѹ��� ������ �����ϰ� ��� �����ߴ�.)
#
#���� : ���������� ���� 1�� �̻� 100,000�� �����̴�.
#       completion�� ���̴� participant�� ���̺��� 1 �۽��ϴ�.
#       �������߿��� ���������� ���� �� �ֽ��ϴ�.
#
#���� :       participant                  |           completion
#       ["leo", "kiki", "eden", "leo"]     |     ["eden", "kiki", "leo"]
#
#��� : "leo" 
#
#�������� : Hash(= Dictionary  in Python) 

def solution(participant, completion):
    dict_h = {index : 0 for index in participant} 
    # ��ųʸ������� key : value �����ε�,, �� dict_h������
    # "leo"�� key �̰� 0�� value��� �� �� �ִ� 
    # dict_h = {"leo" : 0 , "kiki" : 0, "eden" : 0, "leo" : 0} 
    # *��ųʸ����� key���� ����������,, ������ �ִ� key���̶�� �������� �ԷµǴ�
    # key���� ���õȴ�..
    # ��,, participant���� "leo"�� 2���� ���� key:value���·� �ٲ� �ϳ��� ���õǰ� 
    # �Ѱ��� "leo"�� ���ؼ���  key : value�� �����Ѵ�..
    # �׷���,, dict_h�� �Ʒ��� ���� �����ȴ�.
    # dict_h = {"leo" : 0, "kiki" : 0, "eden" : 0}
    

    for i in completion:
        if i in dict_h: 
            dict_h[i] += 1
    # for������ i�� completion���ִ� "eden", "kiki", "leo" ���� ������� ����´�.
    # ���� i�� dict_h�� ����Ǿ��ִ� key���̶��,,
    # dict_h[i] => dict_h["leo"] �� value���� +1 ���� ���Ѷ�,,
    # dict_h = {"leo" : 1 , "kiki" : 1, "eden" : 1} 

    for j in participant:
        if j in dict_h:
            dict_h[j] -= 1
    # for������ j�� participant���ִ� 
    # "leo", "kiki", "eden", "leo"  ���� ������� ����´�.
    # ���� j�� dict_h�� �����Ѵٸ�,,
    # dict_h[j] => dict_h["leo"] �� value���� -1 ���� ���Ѷ�,,
    # �׷���,, participant���� "leo"�� �ι��־,, -1�� �ι� ��Ų��.
    # �׷��� "leo"�� -1�� �ȴ�. 
    # dict_h = {"leo" : -1 , "kiki" : 0, "eden" : 0}
    
    for key, value in dict_h.items():
        if value < 0:
            answer = key
    return answer
    # dict_h.items()���� items()�� dict_h�� key���� value���� ����´�. 
    # key�� "leo"�� ������� value���� "leo"�� value�� 0�� ����´�.
    # ���� �� value�� �����̸�,, �ش� value�� key���� completion�� ��������
    # �ʴ´ٴ� ���� �� �� for������ dict_h�� ���� ���� ���� �� �� �ִ�.
    # �� answer = "leo" �� �� ���̴�.


#2�� �ڵ� (good code)
#import collections,, collections��⿡�� Counter�� 
# �����̳ʿ� ������ ���� �ڷᰡ ����� �ľ��ϴµ� ����ϴ� ��ü��.
# ����Ʈ�� ��Ұ����� collections.Counter()�� �̿��� ���ϸ�
# ����� Dictionary ���·� ��ȯ���ش�..(����..!!)
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

#collections.Counter() ����
# participant = ["leo", "kiki", "eden", "leo"]
# collections.Counter(participant) 
#  ��� =>  {"leo" : 2, "kiki" : 1, "eden" : 1}  
#  ����� ������ ���� �� ���� ������ش�.. �׷��� "leo"�� 2���־ ���� ��(0��° �ε���)
#   key : value ����  (��� : ��� ����) 


#answer => {"leo" : 2, "kiki" : 1, "eden" : 1} - {"eden" : 1, "kiki" : 1, "leo" : 1}
# answer = {"leo" : 1, "kiki" : 0, "eden" : 0}
# list(answer.keys())[0]
# answer.keys() = ["leo", "kiki", "eden"]
# list(answer.keys())[0] �� answer.keys()�� list�� ������,, 0��° �ε����� ����´�..
# ��, "leo"�� ����´�.