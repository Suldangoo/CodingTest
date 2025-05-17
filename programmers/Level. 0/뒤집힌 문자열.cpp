// 프로그래머스 Lv.0 뒤집힌 문자열

#include <string>
#include <algorithm>

using namespace std;

string solution(string my_string) {
    reverse(my_string.begin(), my_string.end());
    return my_string;
}