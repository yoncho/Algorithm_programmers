#문제 : https://programmers.co.kr/learn/courses/30/lessons/42840
#
def solution(answers):
    answer = []
    drop_math_1 = [1, 2, 3, 4, 5]
    drop_math_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    drop_math_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == drop_math_1[i%len(drop_math_1)]:
            count[0] += 1
        if answers[i] == drop_math_2[i%len(drop_math_2)]:
            count[1] += 1
        if answers[i] == drop_math_3[i%len(drop_math_3)]:
            count[2] += 1
    for i in range(len(count)):
        if max(count) == 0:
            return [0]
        if max(count) == count[i]:
            answer.append(i+1)    
    return answer