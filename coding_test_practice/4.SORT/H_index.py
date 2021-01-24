#문제 : https://programmers.co.kr/learn/courses/30/lessons/42747
#
#
#예시 :  citations  |  return
#  [3, 0, 6, 1, 5]        3
def solution(citations):
    count = len(citations)
    #5
    citations.sort(reverse=True)
    #citations = [6, 5, 3, 1 ,0]
    cnt = 0
    for i in range(count, 0, -1):
    #i는 5부터 0 까지 -1씩 적용된다.
        for k in range(len(citations)):
        #citations의 각 인덱스별로 비교해주기위한 for문

            if citations[k] >= i:
                cnt += 1
            #만약 해당 인덱스값이 i보다 크면 , count값보다 더 많은 횟수를 갖고있으면
            # cnt ++를 해준다.

        if cnt >= i:
            return i
        #그렇게 나온 cnt값을 가지고 i와 비교해서 cnt가 크면
        # i값이 문제에서 요구하는 최대 h-index값이므로 return i를 해주면된다.
        cnt = 0
    
    return cnt
    #만약 아무것도 일어나지않으면 cnt는 0을 반환해줘야한다.