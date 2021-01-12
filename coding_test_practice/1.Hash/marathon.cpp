#include <string> // string
#include <vector> //vector
#include <algorithm> //sort

using namespace std;
/*
vector�� �ڵ����� �޸𸮸� �Ҵ��ϴ� �迭�̴�.
vector�� ������ vector<[DATA_TYPE]> [������] �̴�.
��, vector<string>�� string ������ Ÿ���� �迭�� �����Ѵ�.
vector<string> participant�� string Ÿ���� participant��� �迭�� �����Ѵ�.

*�߰�_ ���� ���� ����*
vector<string> participant(10) = string Ÿ���� 10�� ������ �����ִ� participant ����
*/
string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    // string ���� answer���� "" ���ڿ��� �ʱ�ȭ�����ش�.

    /*
    sort�� �����̴�.
    ��� ���´�
    1.sort(arr, arr+n);
    2.sort(v.begin(), v.end()); 
    �� ó������ ������ ������������ �������ش�. 
    3.sort(v.begin(), v.end(), option);  
    option -  1. compare : ����� �����Լ� 
              2. greater<�ڷ���>() : ��������
              3. less<�ڷ���>() : ��������
    */    
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    // participant�� completion�� ������������ �����Ѵ�.

    //completion.size()���� size()�� vectorũ�⸦ �˷��ִ� �Լ��̴�. 
    for(int i=0;i<completion.size();i++)
    {
        /*
        participant �� completion�� ���ؼ�,, ���� �ٸ� ���� �߰ߵǸ�,, 
        �� participant���� �ߺ����̰ų�,, completion�� ���� ������ ���ָ� �� ��
        ����� �ȴ�.
        participant = ["eden", "kiki", "leo", "leo"]
        completion = ["eden", "kiki", "leo"]  
        ���,, for���� �� �Ȱ��� ���Ƽ� �����Եȴ�.
        */
        if(participant[i] != completion[i])
            return participant[i];
    }
    /*
    ���� for���� �� ���Ҵµ�,, �� �����ڸ� �� ã�� ���,, ������ �߱⶧����,
    participant�� �� ������ �ε��� ���� �̿����ڰ� �Ǵ� ���̴�.
    �ᱹ participant�� ������ "leo"�� �̿����ڰ� �Ǵ� ���̴�.
    */
    return participant[participant.size() - 1];
    //return answer;
}