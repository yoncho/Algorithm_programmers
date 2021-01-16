#문제 : https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
#stack & queue 지식 : https://devuna.tistory.com/22
#                     https://jacoblog.tistory.com/2
#
#선행 지식 : stack & queue [ 자료 구조 ]
#            stack = 쌓아올린다, 선입 후출 (LIFO : LAST IN FIRST OUT)
#            queue = 선입 선출 (FIFO : FIRST IN FIRST OUT)
#
# prices 예시 :  [1,2,3,2,3]
#        결과 :  [4,3,1,1,0]
def solution(prices):
    stack = []
    count = 0
    #stack 이라는 빈 리스트를 선언
    #count는 가격이 떨어지지않은 기간의 초를 계산할 변수

    for i in range(len(prices)):
    #len(prices) = 5이므로 i 는 0 ~ 4까지
        for k in range(i + 1, len(prices)):
        #k는 i 이후의 인덱스들을 받아와야하므로,, i+1 ~ 4까지
        #prices[0]을 이제 prices[1]부터 [4]까지 비교해가면서 초를 count해줘야하기때문에
        #for의 range()구조가 위와 같다..

            if prices[i] > prices[k]:
            # 만약 prices[0] 보다 작은 값이면 
            # count 1증가해주고,, for문을 break해서 나간다.
                count += 1
                break
            else:
            # prices[0] 보다 큰 값이면 count 1증가해주고 계속 for문을 작동한다.
                count += 1
        #for문을 나오면 prices[i]에 대한 가격 감소까지의 초가 count된다.
        stack.append(count)
        #그럼 이제 count된 초를 stack에 쌓아준다.
        count = 0
        #그리고 다음 i값을 위해 count를 초기화해준다.
    return stack