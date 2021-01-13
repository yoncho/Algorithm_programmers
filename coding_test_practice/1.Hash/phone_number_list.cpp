#include <string> //for string
#include <vector> //for Vector
#include <unordered_map>  //for unordered_map<type, type> hash_map    
using namespace std;

/*
bool = True or False�� ������ �� �ִ� 1bit �ڷ���
vector<string> phone_book = string������ phone_book ����Ʈ�� ���� ��,, ������ �Ҵ� , �������� �ڵ����� ����

���� ���� :
phone_book = ["12", "456", "1245"]

*/
bool solution(vector<string> phone_book) {
    bool answer = true;

    /*
    unordered_map : 
    map���� �� ���� Ž���� �ϱ� ���� �ڷᱸ��
    �ؽ����̺�� ������ �ڷᱸ���� Ž�� �ð����⵵�� O(1)�̴�.
    �ߺ������͸� ������� �ʴ´�.
    ���� 
    unordered_map<string, int> hash_map = hash_map�̶�� �ؽ� ���̺���(Ű, ����)��
    Ű�� string, ����� int ���� unordered_map �����̴�.
    */
    unordered_map<string, int> hash_map;      
    for(int i = 0; i < phone_book.size(); i++)       //phone_book.size() = 3 �̴�.. 3�� ���� �����ϴϱ�
        hash_map[phone_book[i]] = 1;   
        /*
        ����,, phone_book[0] = "12"
        hash_map = ["12" : 1 , "456" : 1, "1245" : 1] 
        �� ���������.
        */

    for(int i = 0; i < phone_book.size(); i++) {
        string phone_number = "";
        for(int j = 0; j < phone_book[i].size(); j++) {
            /*
            phone_book[i].size() ��
            phone_book[0]�� "12"�̰�,,  phone_book[0].size()�� 2�̴�.
            */
            phone_number += phone_book[i][j];
            /*
            phone_number���� j = 0 ���� ~ 1����,,  phone_book[0][j] ������ ����..
            j = 0�϶�,, phone_number = "1" /  j = 1�϶�,, phone_number = "12" �̷��� ����.
            */

            /*
            �� if���� phone_book = "1245"�϶� �۵��Ѵ�/
            j = 1�϶�,, phone_number = "12" �̰� phone_book = "1245"���� ��������.
            hash_map[phone_number] = hash_map["12"] = 1�̴�. 
            phone_number = "12" �̰� phone_book = "1245" �̹Ƿ� != �̼����Ѵ�.
            ����,, "12"��°� ���ξ�� �ִ� "1245"�� �����ϹǷ�,, answer = false�� �Ǵ� ���̴�.
            */
            if(hash_map[phone_number] && phone_number != phone_book[i])
                answer = false;
        }
    }
    return answer;
}