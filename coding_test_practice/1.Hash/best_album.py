#���� : https://programmers.co.kr/learn/courses/30/lessons/42579#
#operator ����(sorted ����) : https://kkamikoon.tistory.com/138
#reverse ����(sorted ����) : https://kkamikoon.tistory.com/138
#
# genres = ["classic", "classic", "pop"]
# plays = [500, 600, 2000]
#
import operator 
def solution(genres, plays):   
    answer = []
    s = []     
    cmp = []   

    dics = [[key, value] for key, value in zip(plays, genres)]
    #dic�� plays, genres ������ �ϳ��� ���� 2�� ����Ʈ�� ������ش�.
#1   dics = [[500, "classic"], [600, "classic"], [2000, "pop"]]
    
    cnt = {key:0 for key in genres}
    #cnt ���� �帣�� key�������ϰ� value�� 0���� �ʱ�ȭ�����ش�.
    #cnt�� �帣�� play Ƚ���� �� ���� ���Ѵ�.
#2    cnt = {"classic" : 0, "pop" : 0}

    for i in range(len(dics)):
        cnt[dics[i][1]] += dics[i][0] 
    #len(dics) = 3  �̴�.
    #in range(len(dics)) = in range(0, 3 - 1)�� �ǹ��ϸ�
    #�̰� ��,, i�� 0���� 2���� ���ڰ� ���ٴ� ���̴�.
    # dics[0] = [500, "classic"]
    # dics[0][1] = "classic"
    # dics[0][0] = 500 
    # �� ������ �̿��ؼ� ������� cnt�� �� �帣���� �÷��� Ƚ���� ���� �� �����ش�.
    # cnt[dics[0][1]] += dics[i][0]
    # =>  cnt["classic"] += 500    => cnt = {"classic" : 500, "pop" : 0}  �̵ȴ�.
    # 
    # for�� ��� :
#3    cnt = {"classic" : 1100, "pop" : 2000}

    cnt = sorted(cnt.items(), key=operator.itemgetter(1), reverse=True)
    # �帣���� �÷���Ƚ���� �������� ��������������Ѵ�.
    # sorted( ���� )
    # cnt.items()   =  c�Լ��� key-value ���� tuple�� ������ ����Ʈ�� ���ϵȴ�.
    # key=operator.itemgetter(1)   =  cnt���� ����� items() ����Ʈ ������ key,value �̴�.
    #   ���� itemgetter(0)�� �ϸ� ù��°�� ����� key�� �������� �����Ѵٴ� ���̰�,
    #        itemgetter(1)�� �ϸ� �ι�°�� ����� value�� �������� �����Ѵٴ� ���̴�.
    # reverse = True       = reverse�� True�� ���ָ� ��������,,default( �⺻)���� False��
    # 
    # ��� :
#4    cnt = [('pop', 2000), ('classic', 1100)]
    
    for i in range(len(cnt)):
    #i �� len(cnt) = 2  �̹Ƿ� 0 ~ 1���� 

        for k in dics:
            # k�� dics�� ����Ʈ ������ �ϳ��� ����´�.
            # k = [500, "classic"]  ���� k���� [600, "classic"] ������ �ҷ��´�.
            
            if cnt[i][0] == k[1]:
                s.append(k[0])
            # cnt[0][0] = pop
            # k[1] = classic
            # ���� k[1] = pop �̸�  k�� ����� �������� k[0] = value ���� 
            # s��� �� ����Ʈ�� �־��ش�.
            # �� �۾��� Ƚ�� �������� �ɷ��� �帣 ��������,, �� �帣��
            # �÷��� Ƚ���� ����־��ش�.
            # if i = "classic"
#5            s = [500, 600]    �̷��� classic�� �ش��ϴ� play���� ������� �־��ش�.

        s = sorted(s, reverse=True)
        # �� for������ �ش� i ���� play���� �־��� ����Ʈ�� 
        # ������������ �������ش�.
        # ��� :
#6        s = [600, 500]

        for i in range(len(s)):
            # i�� s�� ���� = 2 �̹Ƿ� 0 ~ 1���� 

            if i < 2:
                cmp.append(s[i])
            #�� �帣�� playȽ���� �ִ� 2���� �Է��� �� �ְ��س��Ҵ�.
            # cmp.append(s[i]) => cmp��� ���ڿ���
            # �� �帣�� s ����Ʈ�� �Էµ� ������������ ���ĵ� Ƚ���� 
            # �ִ� 2��������,, cmp�� �־��ش�.
            # ���� �帣�� playȽ���� 1�����̶�� 1���� ����..
            # *Ƚ���� �帣�� ������� ���� �ٸ� ���� ���⶧��,,
            #��� :
#7           cmp = [600, 500]
        
        s = [] 
        # for���� ���������� s ����Ʈ�� �ٽ� �� ����Ʈ�� �ʱ�ȭ���ְ�
        # �ö󰡼� ���� i (=�帣�� for���� �����Ų��.)
      #���
#8    cmp = [2000, 600, 500]
      #cmp�� �帣 �հ� ū �帣���� �� �帣���� �ִ� 2����
      #ū ������� playȽ���� �����ϰ��ִ� ����Ʈ�̴�.  

    for i in range(len(cmp)):  
    #i �� cmp�� ���� = 3 �̹Ƿ� 0 ~ 2����

        for k in range(len(plays)):
        #k�� plays�� ���� = 3 �̹Ƿ� 0 ~ 2����

            if cmp[i] == plays[k]:
            #cmp[i] = [2000, 600, 500]
            #plays[k] = [500, 600, 2000]
            #���� i = 0�϶� k = 0 ~ 2�� �ְ� 
            #cmp[0] = 2000 �� plays[0 ~ 2] �� ���� ���ؼ�
            # ���� ���� ������ �ش� k(play�� �ε���)����
            #answer��� ���� ����Ʈ�� cmp�� ������ ���� plays ����Ʈ��
            # �����ߴ� index ����� �־��ش� !!
            # cmp[0] = 2000�� plays���� index =2�� ���̹Ƿ� answer�� 2���� ���� ����.
            # 
            # �׷��� ���ְ� plays[k] �� 0���� �ʱ�ȭ���ش�.. ������ ���� �ߺ� Ƚ����
            # ��������,, �ε���ó���� ������ �߻��Ѵ�..
                plays[k] = 0
                answer.append(k)
#9  ���� answer = [2, 1, 0]

    #���� return��
    # ������ ������ answer ����Ʈ�� ��ȯ���ش�.
    # answer = [2, 1, 0] �̴�.
    # �ֳ��ϸ� ["classic", "classic", "pop"]
    #           [500, 600, 2000]
    # �� �����̸� classic�� ���� 1100�̰� pop�� ���� 2000�̴�.
    # pop�� �� ũ�Ƿ�,, pop���� 2���� playȽ���� �̾ƿ��µ�,, pop�� playȽ����
    # 1���ۿ� �����Ƿ�,,    cmp�� 2000�� 0��° �ε����� ����
    # �� ���� classic������ 600�� ���� ū ���̰� �� ���������� 500�̹Ƿ�
    # cmp�� 1��° �ε������� 600, 2��° �ε������� 500�� ����.
    # cmp = [2000, 600, 500] �̰�
    # cmp�� plays = [500, 600, 2000] �ϰ� ���ؼ� plays���� �ش簪�� �ε�����
    # answer ����Ʈ�� �־��ָ�,, [2, 1, 0] �̵Ǵ� ���̴�.
    return answer