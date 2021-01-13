#include <string> //for string
#include <vector> //for Vector
#include <unordered_map>  //for unordered_map<type, type> hash_map    
using namespace std;

/*
bool = True or False만 저장할 수 있는 1bit 자료형
vector<string> phone_book = string형태인 phone_book 리스트를 생성 및,, 공간의 할당 , 해제등을 자동으로 해줌

문제 예시 :
phone_book = ["12", "456", "1245"]

*/
bool solution(vector<string> phone_book) {
    bool answer = true;

    /*
    unordered_map : 
    map보다 더 빠른 탐색을 하기 위한 자료구조
    해쉬테이블로 구현한 자료구조로 탐색 시간복잡도는 O(1)이다.
    중복데이터를 허용하지 않는다.
    선언 
    unordered_map<string, int> hash_map = hash_map이라는 해쉬 테이블구조(키, 벨류)로
    키는 string, 밸류는 int 형인 unordered_map 구조이다.
    */
    unordered_map<string, int> hash_map;      
    for(int i = 0; i < phone_book.size(); i++)       //phone_book.size() = 3 이다.. 3개 값이 존재하니까
        hash_map[phone_book[i]] = 1;   
        /*
        참고,, phone_book[0] = "12"
        hash_map = ["12" : 1 , "456" : 1, "1245" : 1] 
        이 만들어진다.
        */

    for(int i = 0; i < phone_book.size(); i++) {
        string phone_number = "";
        for(int j = 0; j < phone_book[i].size(); j++) {
            /*
            phone_book[i].size() 는
            phone_book[0]는 "12"이고,,  phone_book[0].size()는 2이다.
            */
            phone_number += phone_book[i][j];
            /*
            phone_number에는 j = 0 부터 ~ 1까지,,  phone_book[0][j] 값들이 들어간다..
            j = 0일땐,, phone_number = "1" /  j = 1일땐,, phone_number = "12" 이렇게 들어간다.
            */

            /*
            이 if문은 phone_book = "1245"일때 작동한다/
            j = 1일때,, phone_number = "12" 이고 phone_book = "1245"임을 잊지말자.
            hash_map[phone_number] = hash_map["12"] = 1이다. 
            phone_number = "12" 이고 phone_book = "1245" 이므로 != 이성립한다.
            따라서,, "12"라는게 접두어로 있는 "1245"가 존재하므로,, answer = false가 되는 것이다.
            */
            if(hash_map[phone_number] && phone_number != phone_book[i])
                answer = false;
        }
    }
    return answer;
}