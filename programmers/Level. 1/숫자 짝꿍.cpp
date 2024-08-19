// 프로그래머스 Lv.1 숫자 짝꿍

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string X, string Y) {
    vector<char> Xvec(X.begin(), X.end());
    vector<char> Yvec(Y.begin(), Y.end());
    vector<char> nums;
    
    for(int i = 0; i < Xvec.size(); i++)
        for(int j = 0; j < Yvec.size(); j++)
            if(Xvec[i] == Yvec[j]) {
                nums.push_back(Xvec[i]);
                Yvec.erase(Yvec.begin() + j);
                break;
            }
    
    sort(nums.rbegin(), nums.rend()); // 내림차순으로 정렬
    string answer(nums.begin(), nums.end()); // string으로 합치기
    
    return answer;
}