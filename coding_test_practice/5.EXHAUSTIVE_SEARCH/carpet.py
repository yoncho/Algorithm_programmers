#문제 : https://programmers.co.kr/learn/courses/30/lessons/42842
# 
def solution(brown, yellow):
    answer = []
    for i in range(3, (brown + yellow)//3 + 1):
        k = (brown + yellow) // i
        if i <= k and (i - 2) * (k - 2) == yellow:
                answer.append(k)
                answer.append(i)
        if len(answer) == 2:
            break
    return answer