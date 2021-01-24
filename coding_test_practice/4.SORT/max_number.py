#문제 : https://programmers.co.kr/learn/courses/30/lessons/42746
#주어진 숫자배열을 이어 붙여서 가장 큰 숫자 만들기
#
#예시 : numbers
#     [30, 9, 5, 34, 3]
def solution(numbers):
    numbers = list(map(str, numbers))
    #numbers에 str형태의 리스트를 만든다. 
    #numbers = ['30', '9', '5','34', '3']

    numbers.sort(key=lambda x: x*3, reverse=True)
    #number를 정렬하는데 reverse = True 즉, 내림차순정렬(높은 값들 부터,,)
    #key=lambda x : x *3은 x*3을 비교해서 내림차순 정렬하겠다는 것이다,
    # 여기서 왜? x3을 해주냐..?
    # 30, 34, 3의 경우에는 가장 큰수를 만들려면 34 . 3 . 30 순으로 와야한다.
    # 그럼 34 3 30으로 순서를 결정해줄려면 343434 vs 333 vs 303030 으로 각 문자열을 3번정도 이어붙인다음에..
    # 문자열의 비교는 첫번째 인덱스 값부터 비교해간다.
    # 즉 모두 0번째 인덱스는 3으로 동일하다. 그럼 1번째 인덱스는 각 4, 3 , 0이 되므로
    # 34, 3, 30순으로 정렬이된다.
    # numbers = ['9', '5','34', '3', '30'] 이된다.
  
    return str(int(''.join(numbers)))
    #''.join(numbers) = "9534330"이 된다. 하지만 이를 int형으로 바꾼뒤 str로 다시 바꿔줘야한다.
