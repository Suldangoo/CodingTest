// 프로그래머스 Lv.1 신규 아이디 추천
// 2021 KAKAO BLIND RECRUITMENT

#include <string>
#include <cstring>
#include <vector>

using namespace std;

string solution(string new_id) {
    string answer = "";
    // 1단계
    for (char& ch : new_id)
        ch = tolower(ch);
    
    // 2단계
    for (char ch : new_id)
        if (isalpha(ch) ||
            isdigit(ch) ||
            strchr("-_.", ch)) // 해당 문자열이라면
            answer += ch;
    
    // 3단계
    int idx = -1;
    while((idx = answer.find("..")) != -1)
        answer.replace(idx, 2, ".");
    
    // 4단계
    if (answer.front() == '.')
        answer = answer.substr(1);
    if (answer.back() == '.')
        answer = answer.substr(0, answer.size() - 1);
    
    // 5단계
    if (answer.empty())
        answer = "a";
    
    // 6단계
    if (answer.size() > 15)
    {
        answer = answer.substr(0, 15);
        if (answer.back() == '.')
            answer.pop_back();
    }
    
    // 7단계
    while (answer.size() < 3)
        answer += answer.back();
    
    return answer;
}