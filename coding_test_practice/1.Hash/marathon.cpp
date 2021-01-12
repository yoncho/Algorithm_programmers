#include <string> // string
#include <vector> //vector
#include <algorithm> //sort

using namespace std;
/*
vector는 자동으로 메모리를 할당하는 배열이다.
vector의 선언은 vector<[DATA_TYPE]> [변수명] 이다.
즉, vector<string>은 string 데이터 타입의 배열을 생성한다.
vector<string> participant는 string 타입의 participant라는 배열을 생성한다.

*추가_ 공간 선언 가능*
vector<string> participant(10) = string 타입의 10개 공간을 갖고있는 participant 생성
*/
string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    // string 변수 answer에는 "" 빈문자열로 초기화시켜준다.

    /*
    sort는 정렬이다.
    사용 형태는
    1.sort(arr, arr+n);
    2.sort(v.begin(), v.end()); 
    ㄴ 처음부터 끝까지 오름차순으로 정렬해준다. 
    3.sort(v.begin(), v.end(), option);  
    option -  1. compare : 사용자 정의함수 
              2. greater<자료형>() : 내림차순
              3. less<자료형>() : 오름차순
    */    
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    // participant와 completion을 오름차순으로 정렬한다.

    //completion.size()에서 size()는 vector크기를 알려주는 함수이다. 
    for(int i=0;i<completion.size();i++)
    {
        /*
        participant 와 completion을 비교해서,, 서로 다른 곳이 발견되면,, 
        그 participant값이 중복값이거나,, completion에 없는 값으로 완주를 못 한
        사람이 된다.
        participant = ["eden", "kiki", "leo", "leo"]
        completion = ["eden", "kiki", "leo"]  
        경우,, for문이 다 똑같이 돌아서 나가게된다.
        */
        if(participant[i] != completion[i])
            return participant[i];
    }
    /*
    만약 for문을 다 돌았는데,, 미 완주자를 못 찾는 경우,, 정렬을 했기때문에,
    participant의 맨 마지막 인덱스 값이 미완주자가 되는 것이다.
    결국 participant의 마지막 "leo"가 미완주자가 되는 것이다.
    */
    return participant[participant.size() - 1];
    //return answer;
}