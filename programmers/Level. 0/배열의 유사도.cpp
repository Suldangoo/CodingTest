// 프로그래머스 Lv.0 배열의 유사도

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<string> s1, vector<string> s2) {
    int answer = 0;

    for(int i = 0; i < s1.size(); i++) {
        if (find(s2.begin(), s2.end(), s1[i]) != s2.end()) { // 찾지 못한 경우 이터레이터가 end() 반환
            answer++;
        }
    }

    return answer;
}