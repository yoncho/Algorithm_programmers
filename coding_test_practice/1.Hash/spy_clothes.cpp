#include <string>         //for use string
#include <vector>         //for use vector<>
#include <unordered_map>  //for use unordered_map

using namespace std;

int solution(vector<vector<string>> clothes) {
    /*
    clothes = [["ny_cap", "headgear"], ["yellow_cap", "headgear"], ["sunglasses", "eyewear"]]
    */
    
    int answer = 1;

    unordered_map<string, int> attributes;
    // attributes = [ key : value ]

    for(int i = 0; i < clothes.size(); i++)  
        attributes[clothes[i][1]]++;
        /*
        clothes[0][0] = "ny_cap"
        clothes[0][1] = "headgear"
        attributes[clothes[0][1]] = attributes["headgear"]
        attributes["headgear"]++  
        =>   attributes = ["headgear" : 1] 
        이렇게 딕셔너리 구조가 만들어진다.
        */
    /*
    auto는 자동으로 데이터타입을 정해준다..
    즉, it이 정수변수면 int로,,문자열변수면 string으로,, 자동할당 !!
    */
    for(auto it = attributes.begin(); it != attributes.end(); it++)
    /*
    for( it = attributes의 시작 ; it != attributes의 끝; it을 증가)
    
    */
        answer *= (it->second+1);
        /*
        it = attributes는 attributes의 [key]를 가르키는거다
        위 식은 it->first  => key 를 의미하는 것이다..
        it->second => value를 의미 !!
        # "->" 이렇게 해주는 이유는  unordered_map에서는
        # 인덱스로 데이터에 접근할 수 없어서,, -> 참조화살표를
        # 이용해준다.
        answer = (a + 1)*(b + 1)*(c + 1)
        */
    answer--; 
    // answer = (a + 1)*(b + 1)*(c + 1) - 1
    // answer = abc + ab + bc + ca + a + b + c 

    return answer;
}