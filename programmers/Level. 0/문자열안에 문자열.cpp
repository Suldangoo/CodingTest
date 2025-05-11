// 프로그래머스 Lv.0 문자열안에 문자열

#include <string>
#include <vector>

using namespace std;

int solution(string str1, string str2) {
    return (str1.find(str2) == string::npos)?2:1;
}