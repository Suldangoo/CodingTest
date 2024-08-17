// 프로그래머스 Lv.1 월간 코드 챌린지 시즌1 : 내적

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> a, vector<int> b) {
    int answer = 0;
    
    for(int i = 0; i < a.size(); i++) {
        answer += a[i] * b[i];
    }
    
    return answer;
}