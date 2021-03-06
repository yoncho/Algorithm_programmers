#1차 코드
#문제 : 전화번호부에 적힌 전화번호 중, 한번호가 다른 번호의 접두어인 경우가 있는지 확인
#
#조건 : 전화번호부에 적힌 전화번호 배열 배열 => phone_book
#       어떤 번호가 다른 번호의 접두어인 경우,, false반환
#       그렇지 않으면 true 반환
#
#예시 및 예시:      phone_book              return 
#       [119, 97674223, 1195524421]	   |    false
#       [123,456,789]	               |    true
#       [12,123,1235,567,88]	       |    false
#문제 예시 :
#   phone_book
# [ "456", "12", "1245"]
def solution(phone_book):
    p_b = sorted(phone_book)
<<<<<<< HEAD
    #sort = �����Լ�
    # �������� : ����Ʈ.sort() or  y = sorted(x) ����
    # ����Ʈ.sort() ==> ����Ʈ = [ ���� ]   << ������ ������ Ÿ�Ժ��� �������ش�.
    # ���ڴ� ����������,, ���ڴ� ���� ���ĺ�����,, ���ڿ��� �� ���ڿ���,, �ε���������� ���Ͽ� �������ش�.
    # ��,, "12" , "456", "1245" �̷��� ������,, 
    # "1245" �� "456"�� �򰥸���,, ���⼭ ����,,
    # "1245" �� 0��° �ε��� ���� 1�̴�..  "456" �� 0��° �ε��� ���� 4�̴�. ��,, "1245"�� �� Ŀ��������,, 
    # �ȿ��� 0��° �ε����� "456"���� �� ���� ���̱⿡,, "1245"�� ���Ľ� "456"���� �տ� �����Ѵ�..
    # y = sorted(x) ==> x�� ���´� �״�� ���δµ�, y���� x�� [] ���� ������ �����ؼ� ��������ش�.
=======
    #sort = 정렬함수
    # 쓰임형태 : 리스트.sort() or  y = sorted(x) 형태
    # 리스트.sort() ==> 리스트 = [ 내용 ]
    # 숫자는 작은수부터,, 문자는 작은 알파벳부터,, 문자열은 각 문자열별,, 인덱스순서대로 비교하여 정렬해준다.
    # 즉,, "12" , "456", "1245" 이렇게 있을때,, 
    # "1245" 와 "456"이 헷갈린다,, 여기서 보면,,
    # "1245" 의 0번째 인덱스 값은 1이다..  "456" 의 0번째 인덱스 값은 4이다. 즉,, "1245"가 더 커보이지만,, 
    # 안에서 0번째 인덱스는 "456"보다 더 작은 값이기에,, "1245"가 정렬시 "456"보다 앞에 존재한다..
    # y = sorted(x) ==> x의 형태는 그대로 냅두는데, y에는 x의 [] 안의 값들을 정렬해서 저장시켜준다.
>>>>>>> 10e587f2b307a557e9f7c308af36f6597452a1c3
    # 
    # p_b = ["12", "1245", "456"] 

    #zip() 함수
    #동일한 개수로 이루어진 자료형을 묶어주는 역할, 
    # 즉,, for문에서 s1, s2는 서로다른 리스트에서 값을 갖고오는데,,
    # 각각 갖고온걸 서로 짝궁으로 만들어 주고싶다..
    # 예를 들어 
    # name = ["cyh", "kkl"]
    # value = ["90", "100"]
    # for a, b in name, value:
    # 이렇게 해주면 (a, b)는,,
    # ("cyh", "kkl") , ("90", "100") 이된다.. 우리가 원하는건 ("cyh", "90"), ("kkl", "100")인데,,
    # 이걸 해결해주고자 zip()을 사용한다..
    # zip(name, value)를 해주면 이제 원하는 대로,, 각 리스트에서 값들을 하나씩 갖고오는 형태이다.
    # ㄴ> 결과 : ("cyh", "90"), ("kkl", "100")
    #for s1, s2 in zip(a, b) 
    # ㄴs1은 a리스트에서 순서대로 값을 갖고오고, s2는 b에서 순서대로 값을 갖고오는 것이다.
    #
    #for문안에 p_b[1:] 에서 [1:]는 p_b에서 1번인덱스값부터 끝까지만 인식하겠다 의미이다.
    # 만약 [1: 5]라면,, 1번 인덱스부터 5번 인덱스까지만 인식하겠다가 된다. 
    # [1:]에서 [1:빈칸]처럼 빈칸이 들어가면,, 끝까지를 의미한다.
    # s1은 결국 p_b에서 0번째 인덱스부터 , s2는 p_b에서 1번째 인덱스부터 갖고오는 것이다. 

    for s1, s2 in zip(p_b, p_b[1:]): 
        #s1 = "12" ,  s2 = "1245"  을 갖고온 것이다.
        
        #s2.find(s1)은  s2문자열에 s1문자열이 속해있는지 확인하고,,
        #존재한다면,, 시작 인덱스값을 반환한다.
        #그래서 위 s1, s2상황이라면 s2 = "1245" 안에 s1 = "12" 가 
        #s2문자열에서 배열로 따지면 0번째부터 시작하는 것이기때문에 반환값을 0을 준 것이다.
        if s2.find(s1) == 0:
            return False 
    return True

