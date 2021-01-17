#문제 : https://programmers.co.kr/learn/courses/30/lessons/42586
#     
#사용 라이브러리 : math (수학 함수 관련)
#                  math.ceil( x / y )  
#                  : x를 y로 나눴을 때, 소수점 자리가 발생하면 정수에 + 1을 하고 
#                    딱 나눠 떨어지면 해당 정수를 반환해주는 함수이다.
#사용 예시 :   
#    progresse :  [93, 30, 55]
#    speeds    :  [1, 30, 5]       
import math
def solution(progresses, speeds):
    answer = [] 
    day = []
    #각 progresses별로 완성까지 걸리는 날자수를 인덱스별로 넣는 리스트

    first_pix = []
    #day에 정리된 날자수 리스트중 0번째 인덱스를 먼저 집어넣고 처리할 리스트

    for i in progresses:
        day.append(math.ceil((100-i) / speeds.pop(0)))
    # day = [7, 3, 9]
    #  i = 93 이라고 가정하고, speeds.pop(0) = speeds 리스트의 0번째 인덱스값을 pop해옴
    #   speeds = [1, 30, 5]   -> speeds.pop(0) -> speeds = [30, 5]  가된다는 점 유의!!
    #  (100 - i) / speeds.pop(0)        =>     (100 - 93) / 1 = 7
    #  i = 30 일때,, speeds.pop(0) = 30이 된다.
    #  (100 - 30) / 30 => 2.3xx   math.ceil(2.3xx) => 3이 된다. !!!

    first_pix.append(day.pop(0))
    # day = [7, 3, 9]  , day.pop(0) = 7,  first_pix = [7]
    # 이후 day = [3, 9] 가 된다.
    
    for i in day:
    # i = day의 리스트 값들이 하나씩 들어간다.
    # day = [3, 9]
    # i = 3 이라하자.
    #(1) i는 3 다음값 9를 갖고있다.
        if i <= first_pix[0]:
        #만약 그 i값이 고정값 리스트의 0번째 인덱스값보다 작으면 해당 값을 
        # 고정값 리스트에 집어넣는다.
        # i = 3  , first_pix[0] = 7 이므로,, 
        # 성립되서,, first_pix에 넣어준다.
        # first_pix = [7, 3] 인상태로,, (1)로 간다.
        # i = 9일때,, first_pix[0] = 7 보다,, 크므로,,
        # else:문으로 넘어간다. (2)
            first_pix.append(i)
        else:
        #i값이 고정값 리스트 0번째 인덱스보다 작으면
        # first_pix 리스트 길이를 answer에 넣어준다.
        #(2) i = 9인상태, first_pix = [7, 3]이다.
        # answer에는 first_pix의 길이 2가 들어간다.
        # answer = [2]
            answer.append(len(first_pix))
            first_pix = []
            #그러고 first_pix 리스트를 빈 리스트로 만들어준다.
            #그러고 나서 해당 i 값을 빈 first_pix 리스트에 넣어준다.
            #(3) first_pix = [] 빈배열
            first_pix.append(i)
            # 빈리스트에 i = 9 인상태를 넣어준다.
            # first_pix = [9] ,,, 이런 형태로 for문을 돌려주면된다.
  
    answer.append(len(first_pix))
    return answer