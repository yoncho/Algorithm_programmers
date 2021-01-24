#문제 : https://programmers.co.kr/learn/courses/30/lessons/42748
#
#
#sort 함수 구현
def sort(array):
    for i in range(len(array)):
        for k in range(i, len(array)):
            if array[i] > array[k]:
                tmp = array[i]
                array[i] = array[k]
                array[k] = tmp
    return array

def solution(array, commands):
    answer = []
    mid = []
    for i in commands:
        for k in range(len(array)):
            if k >= i[0] - 1 and k < i[1]:
                mid.append(array[k])
        sort(mid)
        answer.append(mid.pop(i[2]-1))
        mid = []
    return answer