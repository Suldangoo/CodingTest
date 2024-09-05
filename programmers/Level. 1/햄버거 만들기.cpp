// 프로그래머스 Lv.1 햄버거 만들기

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> ingredient) {
    vector<int> s;
    vector<int> target = {1, 2, 3, 1};
    int answer = 0;
    
    for (int i : ingredient) {
        // 스택에 하나 삽입
        s.push_back(i);
        
        // 크기가 4 이상이며 1231 순서대로 쌓여있을 경우
        if(s.size() >= 4 && equal(s.end() - 4, s.end(), target.begin())) {
            answer++;
            s.erase(s.end() - 4, s.end()); // 해당 원소 삭제
        }
    }
    
    return answer;
}