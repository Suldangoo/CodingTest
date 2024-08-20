// 프로그래머스 Lv.1 숫자 짝꿍

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string X, string Y) {
    vector<int> X_count(10, 0);
    vector<int> Y_count(10, 0);
    
    for (char c : X) X_count[c - '0']++; // X의 숫자들 빈도 측정
    for (char c : Y) Y_count[c - '0']++; // Y의 숫자들 빈도 측정
    
    vector<char> nums;
    for (int i = 9; i >= 0; --i) {
        int common_count = min(X_count[i], Y_count[i]);
        for (int j = 0; j < common_count; ++j) {
            nums.push_back(i + '0');
        }
    }

    if (nums.empty()) return "-1";
    
    string answer(nums.begin(), nums.end());
    
    if (answer[0] == '0') return "0";
    
    return answer;
}