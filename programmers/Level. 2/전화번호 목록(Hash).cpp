// 프로그래머스 Lv.2 전화번호 목록
// Hash 활용

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

bool solution(vector<string> phone_book) {
    // 1. HashMap을 만든다.
    unordered_map<string, int> map;
    
    for (auto number : phone_book)
        map[number] = 1; // map에 할당
    
    // 2. 모든 전화번호의 substring(접두어)이 HashMap에 존재하는지 확인한다.
    for (int i = 0; i < phone_book.size(); i++)
    {
        for (int j = 1; j < phone_book[i].size(); j++)
        {
            string number = phone_book[i].substr(0, j); // 문자열 슬라이싱
            if (map[number])
                return false; // 하나라도 존재한다면 false를 리턴
        }
    }
    
    // 3. 마지막까지 모두 돌았다면 접두어가 없다는 뜻이다.
    return true;
}