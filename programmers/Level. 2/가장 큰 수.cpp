// 프로그래머스 Lv.2 가장 큰 수

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 비교 함수 정의
bool compare(const string &a, const string &b) {
    return a + b > b + a;
}

string solution(vector<int> numbers) {
    vector<string> v;
    // 1. 모든 숫자 요소들을 문자로 바꾼 후 vector에 모으기
    for (int num : numbers) {
        v.push_back(to_string(num));
    }
    
    // 2. 내림차순으로 문자들 정렬하기
    sort(v.begin(), v.end(), compare);
    
    // 3. answer string에 정렬된 문자열들 합치기
    string answer;
    
    for (string s : v) {
        answer += s;
    }
    
    // 4. 반례 추가하기
    if (answer[0] == '0')
        answer = "0";
    
    return answer;
}