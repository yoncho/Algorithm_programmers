import heapq
def solution(jobs):
    time = 0
    start_time = 0
    finish_time = 0
    sum_task_time = 0

    task_num = 0
    disk = []
    priorities = []
    waiting_tasks = []

    for request in jobs:#힙을 이용하여 우선순위 큐 생성.
        heapq.heappush(priorities,request)

    task_num = len(priorities)

    while True:
        #절대시간 0초부터 시작

        #대기중인 작업 별도관리
        for t in range(len(priorities)):
            if time >= priorities[0][0]:
                waiting_tasks.append(heapq.heappop(priorities))

        #대기중인 작업 작업시간이 적은 순으로 정렬
        waiting_tasks.sort(key = lambda x : x[-1])

        if disk == []:#디스크가 비어있을 때 작업을 넣기위함
            if waiting_tasks != []:
                disk = waiting_tasks.pop(0)
                start_time = time #작업이 시작된 시간을 기록
                finish_time = time + disk[1]

        elif disk != []:#디스크에 작업이 있을때 작업시간이 경과했을 때 작업 삭제
            if time == finish_time :
                sum_task_time += finish_time - disk[0]
                disk = []                

                continue
        time += 1 # 시간의 경과

        if priorities == [] and disk == []:
            break

    return int(sum_task_time/task_num)