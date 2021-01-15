#문제 : https://programmers.co.kr/learn/courses/30/lessons/42579#
#operator 지식(sorted 관련) : https://kkamikoon.tistory.com/138
#reverse 지식(sorted 관련) : https://kkamikoon.tistory.com/138
#
# genres = ["classic", "classic", "pop"]
# plays = [500, 600, 2000]
#
import operator 
def solution(genres, plays):   
    answer = []
    s = []     
    cmp = []   

    dics = [[key, value] for key, value in zip(plays, genres)]
    #dic에 plays, genres 값들을 하나씩 묶어 2중 리스트로 만들어준다.
#1   dics = [[500, "classic"], [600, "classic"], [2000, "pop"]]
    
    cnt = {key:0 for key in genres}
    #cnt 에는 장르를 key값으로하고 value를 0으로 초기화시켜준다.
    #cnt는 장르별 play 횟수의 총 합을 구한다.
#2    cnt = {"classic" : 0, "pop" : 0}

    for i in range(len(dics)):
        cnt[dics[i][1]] += dics[i][0] 
    #len(dics) = 3  이다.
    #in range(len(dics)) = in range(0, 3 - 1)를 의미하며
    #이건 곧,, i에 0부터 2까지 숫자가 들어간다는 것이다.
    # dics[0] = [500, "classic"]
    # dics[0][1] = "classic"
    # dics[0][0] = 500 
    # 위 내용을 이용해서 만들어준 cnt에 각 장르별로 플레이 횟수를 누적 합 시켜준다.
    # cnt[dics[0][1]] += dics[i][0]
    # =>  cnt["classic"] += 500    => cnt = {"classic" : 500, "pop" : 0}  이된다.
    # 
    # for문 결과 :
#3    cnt = {"classic" : 1100, "pop" : 2000}

    cnt = sorted(cnt.items(), key=operator.itemgetter(1), reverse=True)
    # 장르별로 플레이횟수를 기준으로 내림차순해줘야한다.
    # sorted( 내용 )
    # cnt.items()   =  c함수는 key-value 쌍이 tuple로 구성된 리스트가 리턴된다.
    # key=operator.itemgetter(1)   =  cnt에서 갖고온 items() 리스트 순서는 key,value 이다.
    #   만약 itemgetter(0)을 하면 첫번째로 갖고온 key를 기준으로 정렬한다는 것이고,
    #        itemgetter(1)을 하면 두번째로 갖고온 value를 기준으로 정렬한다는 것이다.
    # reverse = True       = reverse에 True를 해주면 내림차순,,default( 기본)값은 False다
    # 
    # 결과 :
#4    cnt = [('pop', 2000), ('classic', 1100)]
    
    for i in range(len(cnt)):
    #i 는 len(cnt) = 2  이므로 0 ~ 1까지 

        for k in dics:
            # k는 dics의 리스트 정보를 하나씩 갖고온다.
            # k = [500, "classic"]  다음 k에는 [600, "classic"] 정보를 불러온다.
            
            if cnt[i][0] == k[1]:
                s.append(k[0])
            # cnt[0][0] = pop
            # k[1] = classic
            # 만약 k[1] = pop 이면  k로 갖고온 정보에서 k[0] = value 값을 
            # s라는 빈 리스트에 넣어준다.
            # 이 작업은 횟수 총합으로 걸러준 장르 순서별로,, 각 장르별
            # 플레이 횟수를 집어넣어준다.
            # if i = "classic"
#5            s = [500, 600]    이렇게 classic에 해당하는 play수를 순서대로 넣어준다.

        s = sorted(s, reverse=True)
        # 위 for문에서 해당 i 값의 play수를 넣어준 리스트를 
        # 내림차순으로 정렬해준다.
        # 결과 :
#6        s = [600, 500]

        for i in range(len(s)):
            # i는 s의 길이 = 2 이므로 0 ~ 1까지 

            if i < 2:
                cmp.append(s[i])
            #각 장르별 play횟수를 최대 2번만 입력할 수 있게해놓았다.
            # cmp.append(s[i]) => cmp라는 빈문자열에
            # 각 장르별 s 리스트에 입력된 내림차순으로 정렬된 횟수를 
            # 최대 2개까지만,, cmp에 넣어준다.
            # 만약 장르에 play횟수가 1번뿐이라면 1개만 들어간다..
            # *횟수는 장르에 상관없이 서로 다른 값을 갖기때문,,
            #결과 :
#7           cmp = [600, 500]
        
        s = [] 
        # for문의 마지막에는 s 리스트를 다시 빈 리스트로 초기화해주고
        # 올라가서 다음 i (=장르로 for문을 진행시킨다.)
      #결과
#8    cmp = [2000, 600, 500]
      #cmp는 장르 합계 큰 장르부터 각 장르별로 최대 2개의
      #큰 순서대로 play횟수를 저장하고있는 리스트이다.  

    for i in range(len(cmp)):  
    #i 는 cmp의 길이 = 3 이므로 0 ~ 2까지

        for k in range(len(plays)):
        #k는 plays의 길이 = 3 이므로 0 ~ 2까지

            if cmp[i] == plays[k]:
            #cmp[i] = [2000, 600, 500]
            #plays[k] = [500, 600, 2000]
            #만약 i = 0일때 k = 0 ~ 2을 넣고 
            #cmp[0] = 2000 과 plays[0 ~ 2] 의 값을 비교해서
            # 같은 값이 있으면 해당 k(play의 인덱스)값을
            #answer라는 최종 리스트에 cmp의 값들을 원래 plays 리스트에
            # 존재했던 index 값들로 넣어준다 !!
            # cmp[0] = 2000은 plays에서 index =2의 값이므로 answer에 2값이 먼저 들어간다.
            # 
            # 그렇게 해주고 plays[k] 는 0으로 초기화해준다.. 이유는 만약 중복 횟수가
            # 들어가있으면,, 인덱스처리에 문제가 발생한다..
                plays[k] = 0
                answer.append(k)
#9  최종 answer = [2, 1, 0]

    #최종 return문
    # 위에서 저장한 answer 리스트를 반환해준다.
    # answer = [2, 1, 0] 이다.
    # 왜냐하면 ["classic", "classic", "pop"]
    #           [500, 600, 2000]
    # 위 조건이면 classic의 합은 1100이고 pop의 합은 2000이다.
    # pop이 더 크므로,, pop부터 2개의 play횟수를 뽑아오는데,, pop은 play횟수가
    # 1개밖에 없으므로,,    cmp에 2000이 0번째 인덱스로 들어간다
    # 그 다음 classic에서는 600이 가장 큰 값이고 그 다음순으로 500이므로
    # cmp에 1번째 인덱스에는 600, 2번째 인덱스에는 500이 들어간다.
    # cmp = [2000, 600, 500] 이고
    # cmp를 plays = [500, 600, 2000] 하고 비교해서 plays에서 해당값의 인덱스를
    # answer 리스트에 넣어주면,, [2, 1, 0] 이되는 것이다.
    return answer