#문제 : https://programmers.co.kr/learn/courses/30/lessons/42626#
#Heap 지식 : https://gmlwjd9405.github.io/2018/05/10/algorithm-heap-sort.html
#Heap 함수 : https://velog.io/@janeljs/python-for-coding-test-6
#
#
#선행 지식 : 힙 (Heap) 정렬
# 
# 예시 : 
#      scoville           |      k      |         return
#  [1, 2, 3, 9, 10, 12]          7                  2
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    #heapq.heapify()는 리스트를 힙으로 만들어주는 함수이다.
    # 입력 리스트 scoville를 힙 scoville로 만들어준다.
    # scoville = [1, 2, 3, 9, 10, 12] 으로 힙이 생성된다.
    # 힙의 구조는  [1]
    #             /   \
    #          [2]     [3]
    #         /  \     /
    #       [9] [10] [12]        이렇게 만들어진다.

    while scoville[0] < K:
    #scoville[0] = 1 < K 이면 while문 작동

        if len(scoville) > 1:
            s1 = heapq.heappop(scoville)
            s2 = heapq.heappop(scoville)
            heapq.heappush(scoville, s1+s2*2)
            answer+=1
        #만약 scoville의 길이가 1 보다 크면 
        # heappop은 heap에서 제일 작은 값을 뽑아온다.
        # s1 = 에는 scoville 에서 제일 작은값 1을 뽑아온다.
        # 그러고나면 scoville에서 제일 작은값은 2가 된다.
        # s2에도 동일하게 scoville에서 제일 작은값 2를 뽑아온다.
        # 그러면 scoville = [3,9,10,12] 가 된다.
        # 그리고 이제 s1 + s2 *2한 값을 scoville에 넣어준다.
        # 1 + 2 * 2 => 5 이다.
        # scoville = [3,5,9,10,12] 가 된다.
        # 위와 같은 방식으로 while문을 돌리면 된다. 
        else:
            return -1
        #만약 scoville가 아무리 작업을 하더라도 k이상의 값을 만들어 내지못해서
        #scoville에 k미만인 값 1개만 남은 상태라면 -1을 리턴해준다.
    return answer