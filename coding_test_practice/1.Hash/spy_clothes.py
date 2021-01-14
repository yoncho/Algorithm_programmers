#문제 : https://programmers.co.kr/learn/courses/30/lessons/42578
#reduce 지식 : https://www.daleseo.com/python-functools-reduce/
#lambda 지식 : https://wikidocs.net/64
#Counter 지식 : https://www.daleseo.com/python-collections-counter/
#
#선행지식 : 1. 한수의 곱셉 
#           (a + 1)*(b + 1)*(c + 1) - 1 = a*b*c + (a*b + b*c + c*a) + (a + b + c)
#           2. collections 라이브러리의 Counter함수
#           3. functools 라이브러리의 reduce함수
from collections import Counter
from functools import reduce 

# clothes는 2중배열이 조건이며,, 옷의 이름 , 옷의 종류 데이터가 입력되어있다.
# clothes = [["NY cap", "headgear"]. ["Yellow_hat", "headgear"], ["sunglasses", "eyewear"]]
def solution(clothes):

    cnt = Counter([kind for name, kind in clothes])
    # [kind for name, kind in clothes] = ["headgear", "headgear", "eyewear"]
#1    Counter(..) = ["headgear" : 2, "eyewear" : 1]    
#     cnt = ["headgear" : 2, "eyewear" : 1]    이렇게 되어있다.
    #         옷의 타입 : 해당 타입의 갯수 in clothes

    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#중   reduce(lambda x, y ....)
#요   reduce는 lambda안의 식에 대하여 누적 계산해준다..
#함   reduce(집계함수, 순회 가능한 데이터[, 초기값])   __기본형태__
#수                                       ** [, 초기값] 은 옵션,, **
    # lambda 인자 : 표현식                             __기본형태__
    # lambda는 인자 : 표현식을 하나의 함수로 만들어준다.
    # lambda는 map(), reduce(), filter() 함수안에서 하나의 함수로 적용된다.
    # cnt는 key : value 형태이다..
    # 즉, 옷의 타입과 타입이 총 몇번 있었는지에 대한 정보를 cnt에 담고있다.
    # cnt.values()는 이제 타입의 갯수가 리스트형태로 저장된다.
    # cnt.values() = [2, 1]
    # 
    # reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    # reduce는 누적합계를 적용시켜준다.. 
    #  
    # lambda 변수 : 계산식,  순회가능한 데이터, 초기값
    # lambda x, y: x*(y+1), cnt.values(), 1
    #
    # x = 1을 초기값으로 넣어주고,, y에는 이제 순차적으로 [2, 1]의 원소들이
    # 들어간다.. 
    # y = 2 받아올때,, 
    #    x = 1 (초기화),   1 * ( 2 + 1 )  => x에 저장
    # y = 1 받아올때,,   
    #    x = 3         ,   3 * ( 1 + 1 )  => x에 저장
    # 최종 x에는 3 * 2 = 6 이 저장된다.
#2    reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1 
    # 위 식은  6 - 1 이므로 5가 나온다.
#3    answer = 5 가된다.
    return answer