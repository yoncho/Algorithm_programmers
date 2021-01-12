#1차 코드
#문제 : participant에는 마라톤에 참여한 선수들의 이름이 담긴 배열 , 
#       completion에는 마라톤을 완주한 선수들의 이름이 담겨있다. 
#       (*단, 마라톤은 단 한명의 선수를 제외하고 모두 완주했다.)
#
#조건 : 참여선수의 수는 1명 이상 100,000명 이하이다.
#       completion의 길이는 participant의 길이보다 1 작습니다.
#       참가자중에는 동명이인이 있을 수 있습니다.
#
#예시 :       participant                  |           completion
#       ["leo", "kiki", "eden", "leo"]     |     ["eden", "kiki", "leo"]
#
#결과 : "leo" 
#
#선행지식 : Hash(= Dictionary  in Python) 

def solution(participant, completion):
    dict_h = {index : 0 for index in participant} 
    # 딕셔너리에서는 key : value 형태인데,, 위 dict_h에서는
    # "leo"가 key 이고 0이 value라고 할 수 있다 
    # dict_h = {"leo" : 0 , "kiki" : 0, "eden" : 0, "leo" : 0} 
    # *딕셔너리에선 key값이 고유값으로,, 기존에 있는 key값이라면 마지막에 입력되는
    # key값이 무시된다..
    # 즉,, participant에서 "leo"가 2개가 각각 key:value형태로 바뀔때 하나는 무시되고 
    # 한개의 "leo"에 대해서만  key : value로 진행한다..
    # 그래서,, dict_h는 아래와 같이 생성된다.
    # dict_h = {"leo" : 0, "kiki" : 0, "eden" : 0}
    

    for i in completion:
        if i in dict_h: 
            dict_h[i] += 1
    # for문에서 i는 completion에있는 "eden", "kiki", "leo" 값을 순서대로 갖고온다.
    # 만약 i가 dict_h에 저장되어있는 key값이라면,,
    # dict_h[i] => dict_h["leo"] 의 value값에 +1 증가 시켜라,,
    # dict_h = {"leo" : 1 , "kiki" : 1, "eden" : 1} 

    for j in participant:
        if j in dict_h:
            dict_h[j] -= 1
    # for문에서 j는 participant에있는 
    # "leo", "kiki", "eden", "leo"  값을 순서대로 갖고온다.
    # 만약 j가 dict_h에 존재한다면,,
    # dict_h[j] => dict_h["leo"] 의 value값에 -1 증감 시켜라,,
    # 그런데,, participant에는 "leo"가 두번있어서,, -1을 두번 시킨다.
    # 그래서 "leo"만 -1이 된다. 
    # dict_h = {"leo" : -1 , "kiki" : 0, "eden" : 0}
    
    for key, value in dict_h.items():
        if value < 0:
            answer = key
    return answer
    # dict_h.items()에서 items()는 dict_h의 key값과 value값을 갖고온다. 
    # key로 "leo"를 갖고오면 value에는 "leo"의 value인 0을 갖고온다.
    # 만약 그 value가 음수이면,, 해당 value의 key값은 completion에 존재하지
    # 않는다는 것을 위 두 for문으로 dict_h에 들어가는 값을 통해 알 수 있다.
    # 즉 answer = "leo" 가 들어갈 것이다.


#2차 코드 (good code)
#import collections,, collections모듈에서 Counter는 
# 컨테이너에 동일한 값의 자료가 몇개인지 파악하는데 사용하는 객체다.
# 리스트의 요소개수를 collections.Counter()를 이용해 구하면
# 결과를 Dictionary 형태로 반환해준다..(개꿀..!!)
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

#collections.Counter() 예시
# participant = ["leo", "kiki", "eden", "leo"]
# collections.Counter(participant) 
#  결과 =>  {"leo" : 2, "kiki" : 1, "eden" : 1}  
#  결과는 갯수가 많은 것 부터 출력해준다.. 그래서 "leo"가 2개있어서 제일 앞(0번째 인덱스)
#   key : value 형태  (요소 : 요소 개수) 


#answer => {"leo" : 2, "kiki" : 1, "eden" : 1} - {"eden" : 1, "kiki" : 1, "leo" : 1}
# answer = {"leo" : 1, "kiki" : 0, "eden" : 0}
# list(answer.keys())[0]
# answer.keys() = ["leo", "kiki", "eden"]
# list(answer.keys())[0] 는 answer.keys()를 list로 만든후,, 0번째 인덱스를 갖고온다..
# 즉, "leo"를 갖고온다.