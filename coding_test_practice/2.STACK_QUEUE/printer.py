#문제 : https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3
#큐 지식 : https://galid1.tistory.com/483 
#          https://www.daleseo.com/python-queue/
#
#선행 지식 : (자료구조)큐
#
#
#예시 : 
#        priorities       |    location
#     [1, 1, 9, 1, 1, 1]          0
from collections import deque
#deque라는 que 함수를 사용하기 위해 import

def solution(priorities, location):
    answer = 0
    s = deque(priorities)
    #priorities로 s라는 큐 구조를 만들었다.
    index_s = deque([i for i in range(len(priorities))])
    #priorities의 인덱스 값들을 갖고 index_s라는 큐 구조를 만들었다.
    ans = []
    #s에 있는 값들을 문제에 의해 처리해서 결과를 넣어줄 큐
    ans_i = []
    #ans에 넣어주는 값들이 priorities에서 갖고있던 인덱스들을 넣어줄 큐 
    count = 0
    
    # s = deque([1, 1, 9, 1, 1, 1])
    # index_s = deque([0, 1. 2. 3. 4. 5])
    while len(s) != 0:

        stay = s.popleft()
        stay_s = index_s.popleft()
        #s.popleft를 하면 s 큐에서 제일 왼쪽에 있는 값을 땐다는 것이다.
        #즉 stay에는 s[0]값인 1이 들어간다.
        #stay_s에는 s[0]의 index값이 들어간다.
        #그러면 s = [1, 9, 1, 1, 1]
        # index_s = [1, 2. 3. 4. 5] 가 된다.
        for i in range(len(s)):
            if stay < s[i]:
                count = 2
                break
            else:
                count = 1
        #len(s) = 4 이므로 i는 0 ~ 4까지 돈다
        # 만약 stay = 1 보다 큰 값이 있으면 count = 2를 넣어주고 for문을 끝낸다.
        # 만약 stay = 1 보다 큰 값이 for문을 끝까지 돌렸을때 없으면 count = 1이 넣어진 상태로 끝난다.
        # 그러면 아래 if문으로 내려가자

        if count == 1:
            ans.append(stay)
            ans_i.append(stay_s)
        if count == 2:
            s.append(stay)
            index_s.append(stay_s) 
        #만약 stay보다 큰 값이 s큐에 있으면 count = 2인 것이고
        # stay보다 큰 값이 s큐에 없으면 count = 1인 것이다.
        #그럼 만약 count = 2이라면 stay보다 큰 값이 s큐에 있으므로
        # 문제가 요구한대로 기존 s큐 끝에 다시 넣어줘야한다.
        # 해당 s값의 인덱스 또한 기존 index_s큐 끝에 다시 넣어준다.
        # 위 상황이라면
        # s = [1, 9, 1, 1, 1, 1]    |    index_s = [1, 2, 3, 4, 5, 0]
        # 이된다.
        # 만약 stay = 9라 가정하자.
        # 그러면 count = 1이된다. stay보다 큰 값이 없기 때문이다.
        # 그러면 stay는 ans에 넣어지게되고, stay가 원래 priorities에서 갖고있던 인덱스 정보도
        #  ans_i큐에 넣어진다.
        # 그러면
        # ans = [9]    |    ans_i = [2]
        # 이렇게 된다.
        # 
        # 예시를 for문 끝까지 돌려 최종 ans와 ans_i를 보면
        # ans   = [9, 1, 1, 1, 1, 1]
        # ans_i = [2, 3, 4, 5, 0, 1]
        # 이된다. 만약 location으로 2가 왔다면 
        # priorties = [1, 1, 9, 1, 1, 1] 에서 인덱스가 2인 값은 9 이다.
        # 그러면 ans에서 9를 출력하는 순서는 1이므로 answer = 1이된다. 

    answer = ans_i.index(location) + 1
    #ans_i.index(location) + 1 == ans_i에서 location에 해당하는 값의 인덱스 번호를 반환해준다.
    return answer