// 프로그래머스 Lv.1 핸드폰 번호 가리기

#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    int length = phone_number.length();
    int visible_count = 4;  // 뒤에 보이는 숫자의 개수
    
    string masked_part = string(length - visible_count, '*');
    string visible_part = phone_number.substr(length - visible_count, visible_count);
    
    return masked_part + visible_part;
}