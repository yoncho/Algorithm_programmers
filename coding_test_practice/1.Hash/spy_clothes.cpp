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
        �̷��� ��ųʸ� ������ ���������.
        */
    /*
    auto�� �ڵ����� ������Ÿ���� �����ش�..
    ��, it�� ���������� int��,,���ڿ������� string����,, �ڵ��Ҵ� !!
    */
    for(auto it = attributes.begin(); it != attributes.end(); it++)
    /*
    for( it = attributes�� ���� ; it != attributes�� ��; it�� ����)
    
    */
        answer *= (it->second+1);
        /*
        it = attributes�� attributes�� [key]�� ����Ű�°Ŵ�
        �� ���� it->first  => key �� �ǹ��ϴ� ���̴�..
        it->second => value�� �ǹ� !!
        # "->" �̷��� ���ִ� ������  unordered_map������
        # �ε����� �����Ϳ� ������ �� ���,, -> ����ȭ��ǥ��
        # �̿����ش�.
        answer = (a + 1)*(b + 1)*(c + 1)
        */
    answer--; 
    // answer = (a + 1)*(b + 1)*(c + 1) - 1
    // answer = abc + ab + bc + ca + a + b + c 

    return answer;
}